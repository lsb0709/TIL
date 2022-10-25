from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    movie_name = models.CharField(max_length=40)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], help_text="0~5사이 값으로 입력하세요")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)