from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('deleteUser/<str:username>/', views.deleteUser, name='deleteUser'),
    path('change_password/', views.change_password, name='change_password')
]