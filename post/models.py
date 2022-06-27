from datetime import datetime 
from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=200,default="")
    content = models.TextField(default="")
    created = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=200, default="")

