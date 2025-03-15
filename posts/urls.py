from django.urls import path
from .views import PostListCreateAPIView, PostLikeListCreateAPIView

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="post-list-create"),
    path('posts/like/', PostLikeListCreateAPIView.as_view(), name='post-like-list'),
]
