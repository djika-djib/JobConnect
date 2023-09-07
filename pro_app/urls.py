from django.urls import path
from . import views

urlpatterns = [
    path('services', views.services, name = "services"),
    path('index', views.index, name = "index"),

]