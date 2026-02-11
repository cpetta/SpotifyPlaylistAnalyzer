# SpotifyPlaylistAnalyzer

Requirements

- docker
- spotify API keys

Setup

1. Add your spotify client id and spotify client secret id to /src/api_keys
2. Run from the command line
```
docker build -t spotify-playlist-analyzer .
```

Usage

1. Run from the command line
```
docker run -it --rm --name spotify-playlist-analyzer spotify-playlist-analyzer
```
3. Right click a playlist in spotify
4. Select `Share`
5. Select `Copy Spotify URI`
6. Example:
```
https://open.spotify.com/playlist/603oF0bPdW4ZwSCHF8Zs4L
```
6. Paste the copied URI into the command window
7. Press Enter
8. Example output below
```
Enter a spotify playlist URL. Formatted like: (open.spotify.com/playlist/)
URL: https://open.spotify.com/playlist/603oF0bPdW4ZwSCHF8Zs4L
Unable to loaded Saved Token requesting new one
requested new token
100%|█████████████████████████████████████████████| 1/1 [00:00<00:00,  4.00it/s]
------------------------------
Top 5 Playlist Genres
------------------------------
18 - downtempo
12 - trip hop
7 - nu jazz
5 - glitch
4 - idm
4 - ambient

Number of artists in playlist: 30 

------------------------------
Top 10 Recommended Artists
------------------------------
100%|███████████████████████████████████████████| 30/30 [00:02<00:00, 13.57it/s]

```
