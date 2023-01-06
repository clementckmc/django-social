from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] # newest items first

    def get_reply_count(self):
        count = Reply.objects.filter(post=self).count()
        if count == 0:
            return "no replies"
        elif count == 1:
            return "1 reply"
        else:
            return f"{count} replies"

    def get_like_count(self):
        return Like.objects.filter(post=self).count()

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.body[0:50]

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
