from typing import Any
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    decription = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=50)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.subject

class Post(models.Model):
    message = models.TextField(max_length=2000)
    Topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message
