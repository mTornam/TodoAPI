from rest_framework import serializers
from core.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
            "due_date",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {"id": {"read_only": True}}
