import os
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from datamodel.models import Application,History,Machine,Software,ConfigModel
from opmanager.CommonPaginator import SelfPaginator
from opmanager.CommonProcessor import execute,distribute

def ListApp(request):
    mList = Application.objects.all()

    # page
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage': lst,
        'request': request,
    }

    return render_to_response('listapp.html', kwvars, RequestContext(request))

def InstallApp(request,ID):

    a = Application.objects.get(id=ID)
    sw = Software.objects.get(id=a.software_id)
    print sw.ins_cmd,a.machine
    log = execute(sw.ins_cmd,a.machine.__str__(),"123456")
    his = History(cmd=sw.ins_cmd, machine=a.machine,log=log)
    his.save()
    a.is_active = True
    a.save()
    return HttpResponseRedirect(reverse('applist'))


def Config(request,ID):

    a = Application.objects.get(id=ID)
    config = ConfigModel.objects.get(id=a.config_model_id)
    config_file = config.tar_pkg
    def_parm = config.def_parm.replace('\r','')
    script = a.script.__str__()
    config_parm = a.config_parm.replace('\r','')
    parm_file = open('parms/test.json', 'w')
    parm_file.write(def_parm)
    parm_file.write('\n')
    parm_file.write(config_parm)
    parm_file.close()
    file_str = config_file.name +' '+script+' '+parm_file.name
    distribute(file_str, a.machine.__str__(), '123456','/opt')
    cmd = 'sh /opt/' + os.path.basename(script) + ' ' + os.path.basename(config_file.name) +' '+ os.path.basename(parm_file.name)
    log = execute(cmd, a.machine.__str__(), "123456")
    his = History(cmd=cmd, log=log, machine=a.machine)
    his.save()
    a.is_config = True
    a.save()
    return HttpResponseRedirect(reverse('applist'))




