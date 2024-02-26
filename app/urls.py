from django.contrib import admin
from django.urls import path
from .views import event_list, add_event
from . import views


urlpatterns = [
    path('', event_list, name='event_list'),
    path('add/', add_event, name='add_event'),
    path('admin/', views.admin, name='admin'),
    path('login/', views.custom_login, name='login'),
     path('logout/', views.custom_logout, name='logout'),  # Add path for logout view
]
