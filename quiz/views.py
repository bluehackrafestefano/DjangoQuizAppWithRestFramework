from rest_framework import generics
from django.shortcuts import render
from .models import Category, Question, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer, QuestionSerializer


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

class QuizDetailView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs['title']
        queryset = Question.objects.filter(quiz__title=title)
        return queryset
