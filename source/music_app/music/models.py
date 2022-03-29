from django.db import models

# Music (id (default), name, producer(s))

# import user (producer(s))
from user.models import User

# Music model
class Music(models.Model):
    name = models.CharField(max_length=200, verbose_name="music_name")
    producer = models.ManyToManyField(User)

    def __str__(self):
        return self.name