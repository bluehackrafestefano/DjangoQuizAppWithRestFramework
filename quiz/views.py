from rest_framework import generics
from django.shortcuts import render
from .models import Category, Question, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer, QuestionSerializer
from .pagination import SmallPageNumberPagination

# Auth:
from rest_framework.permissions import IsAuthenticated , AllowAny


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AllowAny]


class CategoryDetailView(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
    
    # Filtering against the URL:
    def get_queryset(self):
        """
        This view should return a list of all the quizzes for
        the category as determined by the category portion of the URL.
        """
        queryset = Quiz.objects.all()
        category = self.kwargs['category']  # category from url e.g.: quiz/backend
        queryset = queryset.filter(category__name=category)
        return queryset

class QuizDetailView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = SmallPageNumberPagination
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        This view should return a list of all the questions for
        the title as determined by the title portion of the URL.
        """
        queryset = Question.objects.all()
        title = self.kwargs['title']
        queryset = Question.objects.filter(quiz__title=title)
        return queryset
