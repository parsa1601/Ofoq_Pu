from django.urls import path
from . import views

urlpatterns = [
    path('archive/', views.articles_list, name='articles_list')
]
