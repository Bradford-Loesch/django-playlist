from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^', views.index),
    url(r'^', views.index),
    url(r'^', views.index),
]
