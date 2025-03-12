from django.urls import path, include
from rest_framework.routers import DefaultRouter
from categories.views import CategoryViewSet
from comments.views import CommentViewSet
from posts.views import PostViewSet, PostLikeViewSet
from tags.views import TagViewSet
from users.views import UserViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'postlikes', PostLikeViewSet, basename='postlike')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
