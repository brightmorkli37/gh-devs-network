from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.profiles, name='profiles'),
    path('userProfile/<str:pk>/', views.userProfile, name='user-profile'),
    path('account/', views.userAccount, name='account'),
    path('account/edit-profile/', views.editProfile, name='edit-profile'),
]