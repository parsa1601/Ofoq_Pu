from django.contrib import admin
from account.models import Account, NotArticle, ArticleRequest


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ('username', 'first_name', 'last_name', 'organization', 'field')
    search_fields = ('username', 'first_name', 'last_name', 'organization', 'field')
    ordering = ('last_name', 'first_name', 'username')

class NotArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'date')
    list_filter = ('user', 'type', 'date')
    search_fields = ('user', 'type', 'date')
    ordering = ('date',)

class ArticleRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    list_filter = ('user', 'date')
    search_fields = ('user', 'date')
    ordering = ('date',)

admin.site.register(Account, AccountAdmin)
admin.site.register(NotArticle, NotArticleAdmin)
admin.site.register(ArticleRequest, ArticleRequestAdmin)