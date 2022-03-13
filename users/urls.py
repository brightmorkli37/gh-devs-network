from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('userProfile/<str:pk>/', views.userProfile, name='user-profile'),
]
