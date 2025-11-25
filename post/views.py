from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    """
    View to list all posts in the post table to the database
    """
    # model attribute specifies the model to be used to get data from the database
    model = Post
    # template_name renders the html file located at post/list.html
    template_name = 'post/list.html'
    #context_object_name specifies the name of the variable to be used in the template
    context_object_name = 'posts'
    # Order posts by creation date (newest first)
    ordering = ['-created_on']
    # Pagination
    paginate_by = 5

class PostDetailView(DetailView):
    """
    View to display a single post
    """
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'single_post'

class PostCreateView( CreateView):#Post requests
    """
    View to create a new post
    """
    model = Post
    template_name = 'post/new.html'
    
    fields = ['title', 'subtitle', 'body', 'image']
    
    def form_valid(self, form):
        # Set the author to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    """
    View to update an existing post
    """
    model = Post
    template_name = 'post/edit.html'
    fields = ['title', 'subtitle', 'body', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        # Only allow the author to edit their own posts
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(DeleteView):
    """
    View to delete a post
    """
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        # Only allow the author to delete their own posts
        post = self.get_object()
        return self.request.user == post.author