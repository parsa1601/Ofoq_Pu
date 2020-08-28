from django.views import generic
from .models import PDF
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

class IndexView(generic.ListView):
        template_name = "archive\index.html"
        context_object_name = "all_files"

        def get_queryset(self):
            return PDF.objects.all()

def articles_list(request):
    files = PDF.objects.all()
    return render(request, 'archive\index.html',{
        'all_files': files
    })
