from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    intro = models.TextField(blank=True)
    image = ProcessedImageField(
                blank = True,
                upload_to = 'profile/',
                processors = [Thumbnail(300, 300)],
                format = 'JPEG',
                options = {'quality': 90},
    		)