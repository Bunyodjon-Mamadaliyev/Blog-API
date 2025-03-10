from rest_framework import serializers
from .models import Post, PostLike
from tags.models import Tag

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())
    featured_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'tags', 'created_at', 'updated_at', 'status', 'featured_image']
        read_only_fields = ['created_at', 'updated_at']


class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.PrimaryKeyRelatedField(queryset=PostLike.objects.all())
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'user', 'created_at', 'value']
        read_only_fields = ['created_at']


