
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def SelfPaginator(request,List,Limit):
    paginator = Paginator(List, int(Limit))

    page = request.GET.get('page')
    try:
        lst = paginator.page(page)
    except PageNotAnInteger:
        lst = paginator.page(1)
    except EmptyPage:
        lst = paginator.page(paginator.num_pages)

    return lst
