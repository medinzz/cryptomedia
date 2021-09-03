from django.db import models
from users.models import User
from django.utils.text import slugify


class Post(models.Model):
  content = models.TextField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created']

