from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
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
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active: bool = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created: str = models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:
        return self.title

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating: int = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description: str = models.CharField(max_length=200, null=True)
    watchlist: str = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active: bool =models.BooleanField(default=True)
    created: str = models.DateTimeField(auto_now_add=True)
    updated: str = models.DateTimeField(auto_now=True)

    def __str__(self)-> str:
        return f"Rating: {str(self.rating)} - Title: {self.watchlist.title}"