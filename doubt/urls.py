from django.contrib import admin
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^', include('polls.urls')),
    url('polls/', include('polls.urls')),
    url(r'^login/(?P<token>.+)$',views.login,name="login"),
    url('admin/', admin.site.urls),
]

