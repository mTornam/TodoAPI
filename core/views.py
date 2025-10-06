from django.shortcuts import render
from rest_framework import generics
from core.serializers import TaskSerializer
from core.models import Task
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import TaskFilter
from django.contrib.auth import get_user_model

User = get_user_model()


class TasksListCreateView(generics.ListCreateAPIView):
    """
    POST: Creates a new task.
    GET: Returns a list of all tasks.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TaskFilter
    ordering_fields = ["created_at", "due_date", "is_completed"]
    ordering = ["-due_date"]  # default ordering

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

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def get_queryset(self):
        """This view should return a task if it belongs to the currently authenticated user."""
        return Task.objects.filter(user=self.request.user)
