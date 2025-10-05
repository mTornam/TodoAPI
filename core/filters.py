from django_filters import rest_framework as filters
from core.models import Task

class TaskFilter(filters.FilterSet):
    status = filters.BooleanFilter(field_name='is_completed')
    
    class Meta:
        model = Task
        fields = [
            'status', 'due_date'
            #'priority',
            ]