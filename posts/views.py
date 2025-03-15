from rest_framework import generics, permissions
from .models import Post, PostLike
from .serializers import PostSerializer, PostLikeSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostLikeListCreateAPIView(generics.ListCreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

