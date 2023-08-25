from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addlist/', views.addlist, name='addlist'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/editlist/<int:id>', views.editlist, name='editlist'),
    path('deletelist/<int:id>', views.deletelist, name='deletelist'),
]