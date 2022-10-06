from email.policy import default
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=80)
    running_time = models.IntegerField(default=0)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)