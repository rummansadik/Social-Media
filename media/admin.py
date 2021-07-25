from django.contrib import admin
from .models import Comment, Post, News, Notification

admin.site.register(Post)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Notification)
