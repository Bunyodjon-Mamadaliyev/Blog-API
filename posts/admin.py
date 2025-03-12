from django.contrib import admin
from .models import Post, PostLike

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at')
    search_fields = ('title', 'author__user__username', 'category__name')
    list_filter = ('status', 'created_at', 'category')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'value', 'created_at')
    search_fields = ('user__user__username', 'post__title')
    list_filter = ('value', 'created_at')
    ordering = ('-created_at',)
