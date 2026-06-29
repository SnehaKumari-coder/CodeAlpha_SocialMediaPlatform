from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
    )

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers"
    )

    def __str__(self):
        return f"{self.follower} follows {self.following}"