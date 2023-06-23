from django.db import models


# Create your models here.
class Album(models.Model):
    GENRE_CHOICES = [
        ('Rock', 'Rock Music'),
        ('Pop', 'Pop Music'),
        ('Metal', 'Metal Music'),
        ('Jazz', 'Jazz Music'),
        ('R&B', 'R&B Music'),
        ('Country', 'Country Music'),
        ('Dance', 'Dance Music'),
        ('Hip Hop', 'Hip Hop Music'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    image_url = models.URLField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.artist}'
