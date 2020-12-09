from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('first-time/', views.first_time, name='first_time'),
    path('plan-a-visit/', views.plan_visit, name='plan_visit')
]