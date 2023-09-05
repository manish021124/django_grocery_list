from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('deleteUser/<str:username>/', views.deleteUser, name='deleteUser'),
    path('change_password/', views.change_password, name='change_password')
]


# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
