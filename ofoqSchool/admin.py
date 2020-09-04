from django.contrib import admin
from .models import AudioFile

class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'date')
    list_filter = ('creator', 'date')
    search_fields = ('title', 'creator')
    ordering = ('date',)

admin.site.register(AudioFile, AudioAdmin)


