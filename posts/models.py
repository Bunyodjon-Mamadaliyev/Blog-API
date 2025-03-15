from django.db import models
from django.conf import settings
from users.models import UserProfile


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured_image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class PostLike(models.Model):
    LIKE = "like"
    DISLIKE = "dislike"

    VALUE_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    ]
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=10, choices=VALUE_CHOICES)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user} {self.value} {self.post}"

