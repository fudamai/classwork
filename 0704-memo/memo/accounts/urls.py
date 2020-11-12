from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    # 例：/accounts/login/
    path('login/', views.custom_login, name='login'),
    # 例：/accounts/logou/
    path('logout/', views.custom_logout, name='logout'),
    # 例：/accounts/register/
    path('register/', views.custom_register, name='register'),
]