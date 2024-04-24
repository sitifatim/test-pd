from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.ImageField(upload_to='movie_images/')
    duration = models.IntegerField()
    genre = models.JSONField()
    language = models.CharField(max_length=50)
    mpaaRating = models.JSONField(default=dict)
    userRating = models.FloatField()

    class Meta:
        app_label = 'movies'

    def __str__(self):
        return self.name