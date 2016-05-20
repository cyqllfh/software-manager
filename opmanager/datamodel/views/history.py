from datamodel.models import History
from opmanager.CommonPaginator import SelfPaginator
from django.shortcuts import render_to_response,RequestContext

def ListHistory(request):
    mList = History.objects.all()

    # page
    lst = SelfPaginator(request, mList, 20)

    kwvars = {
        'lPage': lst,
        'request': request,
    }

    return render_to_response('listhistory.html', kwvars, RequestContext(request))