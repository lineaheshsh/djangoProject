from django.db import models

# Create your models here.
class Board(models.Model):
    ttl = models.CharField(max_length=50)
    contents = models.TextField()
    writer = models.CharField(max_length=20)