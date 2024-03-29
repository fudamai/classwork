from django.urls import path

from . import views

app_name = 'bbs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('my-page', views.my_page, name='my-page')
]