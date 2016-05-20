import pexpect
import datetime

exp = ['[Pp]assword:', 'continue(yes/no)?', pexpect.EOF, pexpect.TIMEOUT, 'Name or service not known',
'Permission denied', 'No such file or directory', 'No route to host', 'Network is unreachable',
'failure in name resolution', 'No space left on device']

def distribute(filedir, host, password, path, child = None):
	try:
		if not child:
			child = pexpect.spawn('scp -r %s root@%s:%s' % (filedir, host, path), timeout = None)
		index = child.expect(exp)
		if index == 0:
			child.sendline(password)
			return distribute(filedir, host, password, path, child)
		elif index == 1:
			child.sendline('yes')
			return distribute(filedir, host, password, path, child)
		elif index == 2:
			line = child.before
			print 'Line:', line
			print 'Now check the result and return status'
		elif index == 3:
			print 'TIMEOUT Occurred'
			child.kill(0)
			return False
		elif index >= 4:
			child.kill(0)
			print 'ERROR:', exp[index]
			return False
		return True
	except:
		import traceback
		traceback.print_exc()
		print 'Did file finish?', child.exitstatus

exp1 = ['[Pp]assword:', 'continue(yes/no)?', '#', pexpect.EOF, pexpect.TIMEOUT, 'Name or service not known',
'Permission denied', 'No such file or directory', 'No route to host', 'Network is unreachable',
'failure in name resolution', 'No space left on device']
def execute(command, host, password, child = None):
    try:
        if not child:
            child = pexpect.spawn('/usr/bin/ssh', ['root@' + host])
        index = child.expect(exp1)
        if index == 0:
            child.sendline(password)
            return execute(command, host, password, child)
        elif index == 1:
            child.sendline('yes')
            return execute(command, host, password, child)
        elif index == 4:
            print 'TIMEOUT Occurred'
            child.kill(0)
            return 'TIMEOUT'
        elif index >= 5:
            child.kill(0)
            print 'ERROR:', exp1[index]
            return exp1[index]
        elif index == 2:
            print 'login success'
            logname = "/root/" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.log'
            child.sendline(command + " >" + logname)
            result = child.expect(['#'])
            if result == 0:
                child.sendline('cat %s' % logname)
                child.expect("#")
                return child.before
            elif result == 1:
                return 'EOF when exe'
            elif result == 2:
                return 'TIMEOUT when exe'

    except:
        import traceback
        traceback.print_exc()
        print 'Did file finish?', child.exitstatus

