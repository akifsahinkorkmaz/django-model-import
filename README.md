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

## Django Models (for music_app)
