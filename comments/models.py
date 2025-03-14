from django.db import models


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"