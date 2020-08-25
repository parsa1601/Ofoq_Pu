from django.views import generic
from .models import file

class IndexView(generic.ListView):
        template_name = "archive\index.html"
        context_object_name = "all_files"

        def get_queryset(self):
            return file.objects.all()