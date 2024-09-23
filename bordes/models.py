from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    decription = models.CharField(max_length=100)


