from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('author__user__username', 'post__title', 'content')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)
