from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard', views.dashboard),
    url(r'^logout', views.logout),
    url(r'^', views.index),
]
