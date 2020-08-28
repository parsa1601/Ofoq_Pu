from django.views import generic
from .models import Audio_File


class IndexView(generic.ListView):
    template_name = "ofoqSchool\index.html"
    context_object_name = "all_files"

    def get_queryset(self):
        return Audio_File.objects.all()