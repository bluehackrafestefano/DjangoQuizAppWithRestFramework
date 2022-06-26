from rest_framework import generics
from django.shortcuts import render
from .models import Category, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailView(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    
    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs['category']  # category from url e.g.: quiz/backend
        queryset = queryset.filter(category__name=category)
        return queryset
