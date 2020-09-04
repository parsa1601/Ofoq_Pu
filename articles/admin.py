from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    search_fields = ('title', 'author')
    ordering = ('pub_date',)

admin.site.register(Article, ArticleAdmin)


