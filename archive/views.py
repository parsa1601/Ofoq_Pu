from django.views import generic
from .models import file
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

class IndexView(generic.ListView):
        template_name = "archive\index.html"
        context_object_name = "all_files"

        def get_queryset(self):
            return file.objects.all()

def articles_list(request):
    files = file.objects.all()
    return render(request, 'archive\index.html',{
        'all_files': files
    })
