from django.http import HttpResponseRedirect
from django.shortcuts import reverse,render,redirect,HttpResponseRedirect,HttpResponse
from .forms import ArticleForm
from .models import Article,

from django.urls import reverse

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect("/index/")
            return HttpResponseRedirect(reverse('blog:article_detail', args=[str(article.pk), article.slug]))
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create_form.html', {'form': form})





