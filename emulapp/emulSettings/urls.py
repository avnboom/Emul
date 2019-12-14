from django.urls import path

from . import views

urlpatterns = [
    path('xml', views.XmlPost, name='XmlPost'),
]