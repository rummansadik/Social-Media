from django.contrib import admin
from .models import Comment, Post, News

admin.site.register(Post)
admin.site.register(News)
admin.site.register(Comment)
