from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='home'),
    path('<int:id>/delete/', views.TodoDeleteView.as_view(), name='delete'),
    path('<int:id>/check/', views.TodoCheckView.as_view(), name='check'),
    path('<int:id>/', views.TodoModifiView.as_view(), name='modifi'),
    path('<int:id>/update/', views.TodoUpdateView.as_view(), name='update'),
    path('<int:id>/', views.TodoModifiView.as_view(), name='modifi'),
    path('query', views.TodoQueryView.as_view(), name='query'),
    path('add/', views.TodoAddView.as_view(), name='add'),
]