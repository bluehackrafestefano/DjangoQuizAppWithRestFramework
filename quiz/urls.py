from django.urls import path
from .views import CategoryListView, CategoryDetailView, QuizDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('<category>', CategoryDetailView.as_view(), name='category_detail'),
    path('question/<title>', QuizDetailView.as_view(), name='question'),
]