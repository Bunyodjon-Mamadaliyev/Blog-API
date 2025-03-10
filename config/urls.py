"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from categories.views import CategoryViewSet
from comments.views import CommentViewSet
from posts.views import PostViewSet, PostLikeViewSet
from tags.views import TagViewSet
from users.views import UserViewSet, RegisterViewSet, LoginView, RefreshTokenView


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'postlikes', PostLikeViewSet, basename='postlike')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'users', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='register')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]

