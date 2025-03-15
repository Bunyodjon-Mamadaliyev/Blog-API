from django.urls import path
from .views import TagListCreateAPIView

urlpatterns = [
    path("tags/", TagListCreateAPIView.as_view(), name="tag-list-create"),
]
