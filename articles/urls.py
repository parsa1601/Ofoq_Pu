from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.IndexView.as_view() , name='index'),
]
