from django.db.models.base import Model
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, UpdateView, DetailView
from .models import Comment, Post, News, Comment
from .forms import PostForm, CommentForm
from django.views import View
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test


class PostListView(View):

    def get(self, request, *args, **kwargs):
        pc_form = PostForm()
        c_form = CommentForm()
        posts = Post.objects.all().order_by('-date_posted')
        news = News.objects.all().order_by('-date_posted')
        context = {
            'pc_form': pc_form,
            'c_form': c_form,
            'posts': posts,
            'news': news,
        }
        return render(request, 'media/home.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-date_posted')
        news = News.objects.all().order_by('-date_posted')
        pc_form = PostForm(request.POST, request.FILES)
        c_form = CommentForm(request.POST)

        if pc_form.is_valid():
            new_post = pc_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
        context = {
            'pc_form': pc_form,
            'c_form': c_form,
            'posts': posts,
            'news': news,
        }
        return render(request, 'media/home.html', context)


class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        c_form = CommentForm()
        news = News.objects.all().order_by('-date_posted')
        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'c_form': c_form,
            'comments': comments,
            'news': news,
        }
        return render(request, 'media/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        c_form = CommentForm(request.POST)
        news = News.objects.all().order_by('-date_posted')
        if c_form.is_valid():
            new_comment = c_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post': post,
            'c_form': c_form,
            'comments': comments,
            'news': news,
        }
        return render(request, 'media/post_detail.html', context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'image']

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


class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class DisLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if not is_dislike:
            post.dislikes.add(request.user)
        if is_dislike:
            post.dislikes.remove(request.user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class VoteView(View):
    def post(self, request, *args, **kwargs):
        news = News.objects.all().order_by('-date_posted')
        users = User.objects.filter(groups__name='Verified User')
        context = {
            'news': news,
            'users': users
        }
        return render(request, 'media/voting.html', context)

    def get(self, request, *args, **kwargs):
        news = News.objects.all().order_by('-date_posted')
        users = User.objects.filter(groups__name='Verified User')
        context = {
            'news': news,
            'users': users
        }
        return render(request, 'media/voting.html', context)
