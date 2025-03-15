from rest_framework import generics, permissions
from .models import Tag
from .serializers import TagSerializer


class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
