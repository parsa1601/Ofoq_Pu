from django.contrib import admin
from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ('username', 'first_name', 'last_name', 'organization', 'field')
    search_fields = ('username', 'first_name', 'last_name', 'organization', 'field')
    ordering = ('last_name', 'first_name', 'username')

admin.site.register(Account, AccountAdmin)