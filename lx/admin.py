from django.contrib import admin
from .models import Article,Reporter

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','headline','reporter')

admin.site.register(Reporter)