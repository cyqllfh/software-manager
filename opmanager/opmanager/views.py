from django.shortcuts import render_to_response,RequestContext
def home(request):
   return render_to_response('home.html',locals(),RequestContext(request))