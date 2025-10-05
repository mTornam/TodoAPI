from django.urls import path
from .views import RegisterView, TasksListCreateView, TasksDetailView



urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('tasks/', TasksListCreateView.as_view(), name='tasks-list-create'),
    path('tasks/<int:pk>/', TasksDetailView.as_view(), name='tasks-detail'),
]