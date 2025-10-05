from django.shortcuts import render
from rest_framework import generics
from core.serializers import UserSerializer, TaskSerializer
from core.models import Task
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.filters import TaskFilter
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

class RegisterView(generics.CreateAPIView):
    """
        POST: Creates a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TasksListCreateView(generics.ListCreateAPIView):
    """
        POST: Creates a new task.
        GET: Returns a list of all tasks.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = TaskFilter
    ordering_fields = ['created_at', 'due_date']

    def perform_create(self, serializer):
        """Associate the new task with the logged-in user."""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """This view should return a list of all tasks for the currently authenticated user."""
        return Task.objects.filter(user=self.request.user)

class TasksDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        GET: Retrieves a specific task.
        PUT/PATCH: Updates a specific task.
        DELETE: Deletes a specific task.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """This view should return a task if it belongs to the currently authenticated user."""
        return Task.objects.filter(user=self.request.user)
    