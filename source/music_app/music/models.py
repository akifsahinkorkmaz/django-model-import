from django.db import models

# Music (id (default), name, producer(s))

# no need to import user (producer(s))

# Music model
class Music(models.Model):
    name = models.CharField(max_length=200, verbose_name="music_name")
    producer = models.ManyToManyField('user.User')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Save model before adding it to default playlist(s) of producer(s)
        super().save(*args, **kwargs)

        for producer in self.producer.all():
            default_playlist = producer.playlist.get(name= "%s's musics" %producer.name)
            default_playlist.music.add(self)
            default_playlist.save()