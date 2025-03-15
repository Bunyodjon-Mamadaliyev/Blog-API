from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
