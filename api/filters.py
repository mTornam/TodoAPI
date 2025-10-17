from django_filters.rest_framework import FilterSet
from .models import (
    Todo,
    Category,
)


class TodoFilter(FilterSet):
    class Meta:
        model = Todo
        fields = [
            'category',
            'completed',
            # 'created_at',
            # 'updated_at',
        ]


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = [
            'name',
        ]