## ERROR
---

Error's bash output:
```
  File "...\django_music_app\music\models.py", line 10, in <module>
    from user.models import User

  File "...\django_music_app\user\models.py", line 11, in <module>
    from playlist.models import Playlist

  File "...\django_music_app\playlist\models.py", line 10, in <module>
    from music.models import Music

ImportError: cannot import name 'Music' from 'music.models' (...\django_music_app\music\models.py)
```


Code snippets that generates this error:
```python
# music_app/music/models.py (line 6)
from user.models import User
# -------------------------

# music_app/user/models.py (line 6)
from playlist.models import Playlist
# -------------------------

# music_app/playlist/models.py (line 6)
from music.models import Music
# -------------------------
```


The reason behind this error:

```
1. Music model imports User model
2. User model imports Playlist model
3. Playlist model imports Music model
              
                 ||
                _||_
                \  /
                 \/

4. Music model imports User model
5. User model imports Playlist model
6. Playlist model imports Music model

                 ||
                _||_
                \  /
                 \/

4. Music model imports User model
5. ...
6. ...
.
.
.
```


This structure of python modules and imports create a recursive import loop. In real world it just crashes the app because python is trying to import a module that is not ready yet because the module is trying to import another module that is not ready yet because...
