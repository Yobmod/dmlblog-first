"""dmlsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
#import django.contrib.auth.views                #The login views redirect to admin here, or to previous page in dmlmain
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
	
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)), 
	#url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
	#url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),
	
	url(r'^', include('dmlmain.urls')),
	url(r'^blog/', include('dmlblog.urls')),
	url(r'^polls/', include('dmlpolls.urls')),
	url(r'^video/', include('embed_video.urls')),
]

