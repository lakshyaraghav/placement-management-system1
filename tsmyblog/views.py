from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from tsmyblog.models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','body']


class DeletePostView(DeleteView):
    model = Post
    
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')