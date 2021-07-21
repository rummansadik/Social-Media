from django.urls import path
from .views import PostListView, PostUpdateView, PostDetailView, PostDeleteView, NewsListView, NewsDetailView
from media.models import News

urlpatterns = [
    path('', PostListView.as_view(), name='media-home'),
    path('news/', NewsListView.as_view(), name='news'),
    path('post/<int:pk>/', PostDetailView.as_view(extra_context={'news': News.objects.all(
    ).order_by('-date_posted')}), name='post-detail'),
    path('news/<int:pk>/', NewsDetailView.as_view(extra_context={'news': News.objects.all(
    ).order_by('-date_posted')}), name='news-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(extra_context={'news': News.objects.all(
    ).order_by('-date_posted')}), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(extra_context={'news': News.objects.all(
    ).order_by('-date_posted')}), name='post-delete'),
]
