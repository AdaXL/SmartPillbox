from django.conf.urls import url
from . import views

app_name = 'timeset'
urlpatterns = [
	url(r'^index$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<pk>[0-9]+)/setting$', views.SettingView.as_view(), name='setting'),
	url(r'^(?P<patient_id>[0-9]+)/set/$', views.set, name='set'),
    url(r'^$', views.Login),	
    url(r'^ip/$', views.setip, name='setip'),
]
