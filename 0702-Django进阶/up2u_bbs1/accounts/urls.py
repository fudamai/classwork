from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    # ex: /accounts/login/
    path('login/', views.custom_login, name='login'),
    # ex: /accounts/logout/
    path('logout/', views.custom_logout, name='logout'),
    # ex: /accounts/register
    path('register/', views.custom_register, name='register'),
    # ex: /accounts/userprofile
    path('userprofile/', views.userprofile, name='userprofile')
]