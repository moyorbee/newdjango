from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from blog.models import Post



# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/post-list.html"
    


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post-form.html"

class PostDetailView(DetailView):
    model = Post  
    template_name =  "blog/post-detail.html" 


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "blog/post-form.html"

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy()
    template_name = "blog/post-confirm-delete.html"
    
    



