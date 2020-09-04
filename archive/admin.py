from django.contrib import admin
from .models import PDF

class PdfAdmin(admin.ModelAdmin):
    list_display = ('title', 'jalali_publish')
    list_filter = ('date',)
    search_fields = ('title',)
    ordering = ('date',)

admin.site.register(PDF, PdfAdmin)
