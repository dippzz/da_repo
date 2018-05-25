from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', views.registerSubmit),
    url(r'^login', views.loginUser)
]