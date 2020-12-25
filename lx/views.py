from django.shortcuts import render

from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Article

class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
