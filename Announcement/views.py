from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post



def home(request):
    context = {
        # pylint: disable=maybe-no-member
        'posts': Post.objects.all()
    }
    return render(request,'announcement/home.html',context)

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name='Announcement/home.html'  # <app/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name='Announcement/user_posts.html'  # <app/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # pylint: disable=maybe-no-member
        return Post.objects.filter(author=user).order_by('-date_posted')




class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False







# Create your views here.
