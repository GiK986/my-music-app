from django.db import models
from my_music_app.user_profile.validators import validate_username


# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=15
                                , validators=[validate_username])

    email = models.EmailField()

    age = models.PositiveIntegerField(blank=True, null=True)