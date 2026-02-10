# SpotifyPlaylistAnalyser

Currently requires an additional ``settings.py`` that contains a spotify API id and secret formatted like

```
class Settings:
	def __init__(self):
		self.id:str = ""
		self.secret:str = ""
```

Setup
```
docker build -t spotify-playlist-anilyzer .
```

Usage
1. Run ``docker run -it --rm --name spotify-playlist-anilyzer spotify-playlist-anilyzer``
2. Right click a playlist in spotify
3. Select cShare``
4. Select ``Copy Spotify URI``
5. Example: ``https://open.spotify.com/playlist/603oF0bPdW4ZwSCHF8Zs4L``
6. Paste the copied URI into the command window
7. Press Enter
