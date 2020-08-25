
from django.http import HttpResponse
from django.views import generic
from .models import Article


class IndexView(generic.ListView):
    template_name = "articles\index.html"
    context_object_name = "text"

    def get_queryset(self):
        return Article.objects.all()

def articles_list(request):
    return HttpResponse("Temporary layout for the articles menu")
#hello guys :)