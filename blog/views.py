from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import BlogPost
from django.views import generic
from django.db.models import Q
# Create your views here.


# Home View
class HomeView(generic.ListView):
    model = BlogPost
    template_name = 'home.html'

class DetailView(generic.DetailView):
    model = BlogPost
    template_name = 'details.html'

class CreatePostView(generic.CreateView):
    model = BlogPost
    template_name = 'create_post.html'
    fields = '__all__'

class SearchView(generic.ListView):
    model = BlogPost
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("query")
        search_list = BlogPost.objects.filter(Q(title__contains=query))
        return search_list

    
