from django.urls import path
from django.conf.urls import url

from . import views

#app_name = 'polls'
urlpatterns = [
    path('', views.signin, name='signin'),
     url(r'^login/(?P<token>.+)$',views.login,name="login"),
	url(r'^index/', views.index, name='index'),
	url(r'^courses/', views.courses, name='courses'),
	url(r'^trendingquestions/' , views.trendingquestions, name='trendingquestions'),
    url(r'^users/', views.users, name='users'),
    url(r'^selectedtopic/', views.selectedtopic, name='selectedtopic'),
	url(r'^selectedtopic1/', views.selectedtopic1, name='selectedtopic1'),
	url(r'^selectedtopic2/', views.selectedtopic2, name='selectedtopic2'),
	url(r'^selectedtopic3/', views.selectedtopic3, name='selectedtopic3'),
	url(r'^viewqa/' , views.viewqa , name = 'viewqa'),
	url(r'^digi/' , views.digi , name = 'digi'),
	url(r'^vlsi/' , views.vlsi , name = 'vlsi'),
	url(r'^dsp/' , views.dsp , name = 'dsp'),
	url(r'^ls/' , views.ls , name = 'ls'),
	url(r'^viewqa1/',views.viewqa1,name = 'viewqa1'),
	url(r'^viewqa2/',views.viewqa2,name = 'viewqa2'),
	url(r'^viewqa3/',views.viewqa3,name = 'viewqa3'),
	url(r'^details/',views.details,name = 'details'),
	url(r'^profile/',views.profile,name = 'profile'),
	url(r'^myquestions/',views.myquestions,name = 'myquestions'),

]
