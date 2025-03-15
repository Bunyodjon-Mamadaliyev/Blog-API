from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

