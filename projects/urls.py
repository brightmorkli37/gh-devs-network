from django.urls import path
from . import views


# app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project_detail/<str:pk>/', views.project_detail, name='details'),
    path('projects/add_new/', views.add_project, name='add-project'),
    path('projects/update_project/<str:pk>/', views.update_project, name='update-project'),
    path('projects/delete/<str:pk>/', views.delete_project, name='delete-project'),
]