from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.views




urlpatterns = [
	url(r'^$', views.homepage, name='homepage'),

	url(r'^contact/$', views.contact_admins, name='contact_admins'),
	url(r'^admin/$', views.django_admin_page, name='django_admin_page'),
	url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
	url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
