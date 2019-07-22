from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.models import Post, PostReaction, CommentReaction, Comment, User

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(PostReaction)
admin.site.register(Comment)
admin.site.register(CommentReaction)
