from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()

    image = models.ImageField(blank=True, upload_to='images/')

    # 사용자가 썸네일 이미지도 함께 선택해야 한다.
    # image를 원본으로 썸네일 이미지를 만드려면 ImageSpec
    thumbnail = ProcessedImageField(
        upload_to='images/',
        blank=True,
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 90}
    )