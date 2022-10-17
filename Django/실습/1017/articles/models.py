from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(120, 60)])