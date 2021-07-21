from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, UpdateView, DetailView
from .models import Post, News
from .forms import PostForm
from django.views import View


class PostListView(View):

    def get(self, request, *args, **kwargs):
        pc_form = PostForm()
        posts = Post.objects.all().order_by('-date_posted')
        news = News.objects.all().order_by('-date_posted')
        context = {
            'pc_form': pc_form,
            'posts': posts,
            'news': news,
        }
        return render(request, 'media/home.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-date_posted')
        news = News.objects.all().order_by('-date_posted')
        pc_form = PostForm(request.POST)

        if pc_form.is_valid():
            new_post = pc_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
        context = {
            'pc_form': pc_form,
            'posts': posts,
            'news': news,
        }
        return render(request, 'media/home.html', context)


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NewsListView(View):
    def get(self, request, *args, **kwargs):
        news = News.objects.all().order_by('-date_posted')
        context = {
            'news': news,
        }
        return render(request, 'media/news.html', context)

    def post(self, request, *args, **kwargs):
        news = News.objects.all().order_by('-date_posted')
        context = {
            'news': news,
        }
        return render(request, 'media/news.html', context)


class NewsDetailView(DetailView):
    model = News
