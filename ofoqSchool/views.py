from django.views import generic
from .models import AudioFile


class IndexView(generic.ListView):
    template_name = "ofoqSchool\index.html"
    context_object_name = "all_files"

    def get_queryset(self):
        return AudioFile.objects.all()