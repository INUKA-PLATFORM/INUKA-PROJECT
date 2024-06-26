from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.user_login, name='login'),
    
    path('admin/', views.admin, name='admin'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('public_register/', views.public_register, name='register'),
    
    path('login/', views.user_login, name='login'),
]