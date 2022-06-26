from django.urls import path
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('<category>', CategoryDetailView.as_view(), name='category_detail'),
]