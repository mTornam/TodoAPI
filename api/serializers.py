from rest_framework import serializers
from .models import Todo, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "is_default": {"read_only": True},
        }


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "title",
            "description",
            "category",
            "completed",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]