from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import Task

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            }
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'due_date', 'created_at', 'updated_at']
        extra_kwargs = {'id': {'read_only': True}}
        