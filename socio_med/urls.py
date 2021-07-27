"""socio_med URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from media.models import News
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),

    path('profile/', user_views.profile, name='profile'),
    path('profile_edit/', user_views.profile_edit, name='profile_edit'),
    path('login/', auth_views.LoginView.as_view(extra_context={'news': News.objects.all(
    ).order_by('-date_posted')}, template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(extra_context={'news': News.objects.all(
    ).order_by('-date_posted')}, template_name='users/logout.html'), name='logout'),
    path('', include('media.urls')),
    path('^inbox/notifications/',
         include(notifications.urls, namespace='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
