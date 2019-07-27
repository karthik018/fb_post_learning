import uuid

from django.db import models
from fb_post.reactions import Reaction
from django.utils import timezone as t
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pic = models.CharField(max_length=100)
    mobile_number = models.TextField(max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_content = models.CharField(max_length=300)
    post_create_date = models.DateTimeField(auto_now=t.now())

    def __str__(self):
        return self.post_content


class PostReaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=5, choices=Reaction.getreactions())

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return self.reaction


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_on = models.ForeignKey('self', blank=True, null=True,
                                     on_delete=models.CASCADE)
    comment_create_date = models.DateTimeField(auto_now=t.now())
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.message


class CommentReaction(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=5, choices=Reaction.getreactions())

    class Meta:
        unique_together = ('comment', 'user')

    def __str__(self):
        return self.reaction


class Person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    person_id = models.UUIDField(unique=True, default=uuid.uuid4())
