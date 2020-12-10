from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('first-time/', views.first_time, name='first_time'),
    path('plan-a-visit/', views.plan_visit, name='plan_visit'),
    path('plan-a-visit/success/', views.visit_success, name='visit_success '),
    path('sermons/', views.sermons, name='sermons'),
    path('watch/', views.watch, name='watch'),
    path('auth/login/', views.log_in, name="login"),
    path('auth/signup/', views.signup, name="signup"),
    path('auth/logout/', views.log_out, name="logout"),
]
