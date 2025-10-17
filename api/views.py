from rest_framework import generics, filters
from drf_spectacular.utils import extend_schema
from .models import (
    Todo,
    Category,
)
from .serializers import (
    TodoSerializer,
    CategorySerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TodoFilter
from .pagination import CustomPagination


# Create your views here.
@extend_schema(tags=['Categories'])
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_anonymous:
            serializer.save(user=self.request.user)


@extend_schema(tags=['Categories'])
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@extend_schema(tags=['Todos'])
class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,]
    filterset_class = TodoFilter
    ordering_fields = ['created_at', 'title', 'category']
    pagination_class = CustomPagination

@extend_schema(tags=['Todos'])
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer