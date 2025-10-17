from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreate.as_view()),
    path('categories/<int:pk>', views.CategoryDetail.as_view()),
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoDetail.as_view()),
]
