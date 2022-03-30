# Django Model Import

When starting a new project, structuring data and logic is an important part of development. In Django structuring data is done with models. And logic part with urls, views, etc... Django models can have logic in them too.

The purpose of this project is showing what can go wrong when creating models in Django. And teaching system design skills to overcome this challenges. A music app will be created in this tutorial for demonstration purposes.

Frontend for music app is not a part of this tutorial.

## About Music App

The music app should have music, producers or listeners (users) and playlist at minimum complexity.

Music:
-   Music was produced by producers. Therefore music has producer(s). 
-   Music has a name.

Playlist:
-   Playlists are a collection for musics. Therefore playlist has music(s).
-   Playlist has a name.

User (producer or listener):
-   User can create playlist. User has a default playlist for musics they produced. Therefore user has playlist(s).
-   User has a name.

This structure (model) of data given above might not be the best solution out there for a music app. The data structure of the music app is modelled that way because it coincides with tutorial's purpose. 

## Setup

Setup a Django project with 3 additional django apps (music, user, playlist). 

---
- `music_app` is the Django project's name in this tutorial. 

- `source/music_app` is the path of Django project.

- See `Setup.md` for further information.
---

## Django Models (see `old_models_music_app/...`)

### Music:
In `music_app/music/models.py` create a music model as:
```python
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

    def save(self, *args, **kwargs):
        # Save model before adding it to default playlist(s) of producer(s)
        super().save(*args, **kwargs)

        for producer in self.producer.all():
            default_playlist = producer.playlist.get(name= "%s's musics" %producer.name)
            default_playlist.music.add(self)
            default_playlist.save()
```

Register model in `music_app/music/admin.py` as:

```python
from django.contrib import admin
from .models import Music

# Register Music model
admin.site.register(Music)
```

### Playlist:
In `music_app/playlist/models.py` create a playlist model as:
```python
from django.db import models

# Playlist (id (default), name, music(s))

# import music
from music.models import Music

# Playlist model
class Playlist(models.Model):
    name = models.CharField(max_length=200, verbose_name="playlist_name")
    music = models.ManyToManyField(Music)

    def __str__(self):
        return self.name
```

Register model in `music_app/playlist/admin.py` as:

```python
from django.contrib import admin
from .models import Playlist

# Register Playlist model
admin.site.register(Playlist)
```

### User:
In `music_app/user/models.py` create a user model as:
```python
from django.db import models

# User (id (default), name, playlist(s))

# import playlist
from playlist.models import Playlist

# User model
class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="user_name")
    playlist = models.ManyToManyField(Playlist)

    def save(self, *args, **kwargs):
        # Save model before creating a default playlist
        super().save(*args, **kwargs)

        # If model is newly created
        try: 
            self.playlist.get(name="%s's musics" %self.name)
        except:
            default_playlist = Playlist(name="%s's musics" %self.name)
            default_playlist.save()
            self.playlist.add(default_playlist)

    def __str__(self):
        return self.name
```

Register model in `music_app/user/admin.py` as:

```python
from django.contrib import admin
from .models import User

# Register User model
admin.site.register(User)
```

### Make migrations:

- Make migrations and migrate.
- See `Setup.md` for further information.

## Error

There is an error. For further information see `Error.md`.

## Old Codes

- The code that contains old models that create an error can be seen at `old_models_music_app/...`.
- The code in `source/music_app/...` will be redesigned.

## Better Django Models

Since models given above create error, redesigning model structures is necessary. Althoug fields of music, user and playlist models are same, implementation and coding of modules should change. To break import loop (see `Error.md`), using unnecessary imports for models should avoided. 

Django is a highly opinionated framework. Which means, Django usually has a specific way to implement the solution to any given problem. This is what makes Django robust and fast for development. Django-models are no different. Django should handle foreign models wherever possible.


### Music:
In `music_app/music/models.py` change music model as:
```python
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
```

### Playlist:
In `music_app/playlist/models.py` change playlist model as:
```python
from django.db import models

# Playlist (id (default), name, music(s))

# no need to import music

# Playlist model
class Playlist(models.Model):
    name = models.CharField(max_length=200, verbose_name="playlist_name")
    music = models.ManyToManyField('music.Music')

    def __str__(self):
        return self.name
```

### User:
In `music_app/user/models.py` change user model as:
```python
from django.db import models

# User (id (default), name, playlist(s))

# importing playlist is necessary
# Playlist class will be used on save method!
from playlist.models import Playlist

# User model
class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="user_name")
    playlist = models.ManyToManyField('playlist.Playlist')

    def save(self, *args, **kwargs):
        # Save model before creating a default playlist
        super().save(*args, **kwargs)

        # If model is newly created
        try: 
            self.playlist.get(name="%s's musics" %self.name)
        except:
            default_playlist = Playlist(name="%s's musics" %self.name)
            default_playlist.save()
            self.playlist.add(default_playlist)

    def __str__(self):
        return self.name
```

### Make migrations (Again):

- Make migrations and migrate.
- See `Setup.md` for further information.

----
Migration process should be successful.

---

## Test:

- Run django development server.
- Create superuser
- Visit admin panel
- Test models

## Error:

Django admin module should force you to:
-   create/add a playlist when creating user
-   create/add a user when creating music
-   create/add a music when creating playlist

The reasen behind this is:
-   user model has playlist field that can not be empty 
-   music model has user field that can not be empty 
-   playlist model has music field that can not be empty 

The needs of music_app is:
-   A music always has a producer even if it is anonym. 

-   And user always has a playlist for songs they produced. But the default playlist is already enforced for user models with custom save method. Therefore there is no need to enforce it on field level.

-   A playlist can be empty.

The needs of user and playlist apps and implementation of models are not coinciding.

## Better Django Models 2

Since music model is spot on, it does not need to change.

### Playlist:
In `music_app/playlist/models.py` change playlist model as:
```python
from django.db import models

# Playlist (id (default), name, music(s))

# no need to import music

# Playlist model
class Playlist(models.Model):
    name = models.CharField(max_length=200, verbose_name="playlist_name")
    # music can be null or blank
    music = models.ManyToManyField('music.Music', blank=True)

    def __str__(self):
        return self.name
```

### User:
In `music_app/user/models.py` change user model as:
```python
from django.db import models

# User (id (default), name, playlist(s))

# importing playlist is necessary
# Playlist class will be used on save method!
from playlist.models import Playlist

# User model
class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="user_name")
    # playlist can be null or blank. 
    playlist = models.ManyToManyField('playlist.Playlist', blank=True)


    def save(self, *args, **kwargs):
        # Save model before creating a default playlist
        super().save(*args, **kwargs)

        # If model is newly created
        try: 
            self.playlist.get(name="%s's musics" %self.name)
        except:
            default_playlist = Playlist(name="%s's musics" %self.name)
            default_playlist.save()
            self.playlist.add(default_playlist)

    def __str__(self):
        return self.name
```

### Make migrations (Again):

- Make migrations and migrate.
- See `Setup.md` for further information.

----
Migration process should be successful.

----

## Test:

- Run django development server.
- Create superuser
- Visit admin panel
- Test models

----
Test should be successful.

----

## Django Model Importer

For further information on how django import models, see `Django-model-importer.md`.


## Other Tips

This structure and implementation of models are not the best practices. There is unsolved problems in data structure and logic of music app. Since this tutorial is focusing on model imports, other problems will not be argued extensively. 

### Some of the problems that can occur:

1) When using additional logic on model's built-in methods being careful is suggested.

In this tutorial, while updating user models, superuser must select the "user's musics" playlist as well as user's other playlists. Otherwise another "user's musics" playlist will be created and user's other playlists are lost during the saving process. This can be prevented with more additional logic on model's built-in methods and some type of state for models.

