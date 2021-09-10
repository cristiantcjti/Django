from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name: str = models.CharField(max_length=30)
    about: str = models.CharField(max_length=150)
    website: str = models.URLField(max_length=100)

    def __str__(self)-> str:
        return self.name
class WatchList(models.Model):
    title: str = models.CharField(max_length=50)
    storyline: str = models.CharField(max_length=200)
    active: bool = models.BooleanField(default=True)
    created: str = models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:
        return self.title