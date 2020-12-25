from django.urls import path
from .views import ArticleDetailView

urlpatterns = [
    path('', ArticleDetailView.as_view(), name='article-detail'),
]
