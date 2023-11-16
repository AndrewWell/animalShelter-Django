from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cats', views.cats, name='cats'),
    path('dogs', views.dogs, name='dogs'),
    path('contacts', views.contacts, name='contacts'),
    path('how2Help', views.how2Help, name='how2Help')
]
