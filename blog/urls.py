from django.urls import path, re_path
from . import views
 
app_name = 'blog'
urlpatterns = [
    # 展示所有文章
    path('/index/', views.ArticleListView.as_view(), name='article_list'),
    # 展示文章详情
    re_path('article/(?P<pk>\d+)/(?P<slug1>[-\w]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
    # 添加文章
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
]
