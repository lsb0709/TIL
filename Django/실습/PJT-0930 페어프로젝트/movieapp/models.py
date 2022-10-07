from statistics import mode
from turtle import title, update
from venv import create
from xmlrpc.client import DateTime
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hearted = models.BooleanField(default=False)
