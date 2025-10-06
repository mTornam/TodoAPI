from django.urls import path
from .views import TasksListCreateView, TasksDetailView


urlpatterns = [
    path("tasks/", TasksListCreateView.as_view(), name="tasks-list-create"),
    path("tasks/<int:pk>/", TasksDetailView.as_view(), name="tasks-detail"),
]
