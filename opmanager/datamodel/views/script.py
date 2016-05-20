import os
from django.core.urlresolvers import reverse
from datamodel.models import Script,Machine,History
from django.http import HttpResponseRedirect
from opmanager.CommonPaginator import SelfPaginator
from django.shortcuts import render_to_response,RequestContext
from opmanager.CommonProcessor import distribute, execute

def ListScript(request):
    mList = Script.objects.all()

    # page
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage': lst,
        'request': request,
    }

    return render_to_response('listscript.html', kwvars, RequestContext(request))

def RunScript(request,ID):

    q = Script.objects.filter(id=ID)
    a = Script.objects.get(id=ID)
    filepath = q.get().script_file.__str__()
    basename = os.path.basename(filepath)
    for i in q:
        for m in i.machines.all():

            flag = distribute(filepath,m.__str__(), "123456","/root")
            if flag is False:
                print "distribute" + filepath + " to " + m.__str__() + " failed!!!"
                continue
            log = execute("sh /root/"+basename, m.__str__(), "123456")

            machine = Machine.objects.get(ip=m.__str__())
            cmd = "sh " + filepath
            his = History(cmd=cmd, log=log, machine=machine)
            his.save()

    a.is_run = True
    a.save()
    return HttpResponseRedirect(reverse('scriptlist'))