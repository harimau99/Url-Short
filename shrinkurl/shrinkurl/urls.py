from django.conf.urls import include, url
from django.contrib import admin
from shrink import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name="home"),
    url(r'^shrinkurl/$',views.shrink,name="shrinkurl"),
    url(r'^(?P<inputURL>[0-9a-zA-Z]+)/$',views.retrieve,name="virivu"),
]