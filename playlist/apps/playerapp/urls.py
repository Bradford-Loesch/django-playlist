from django.conf.urls import url
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', views.index),
]