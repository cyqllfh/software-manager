"""opmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from opmanager.views import home
from datamodel.views import app,history,script

urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^file/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^app/list/',app.ListApp, name='applist'),
    url(r'^app/install/(?P<ID>\d+)/$', app.InstallApp, name='installurl'),
    url(r'^app/config/(?P<ID>\d+)/$', app.Config, name='configurl'),
    url(r'^history/list/', history.ListHistory, name='historylist'),
    url(r'^script/list/', script.ListScript, name='scriptlist'),
    url(r'^script/run/(?P<ID>\d+)/$', script.RunScript, name='runurl'),
]
