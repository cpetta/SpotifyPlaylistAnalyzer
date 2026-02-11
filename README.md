# SpotifyPlaylistAnalyzer

Requirements

- docker
- spotify API keys

Setup

1. Add your spotify client id and spotify client secret id to /src/api_keys
2. ```
   docker build -t spotify-playlist-analyzer .
   ```

```

Usage

1. Run `docker run -it --rm --name spotify-playlist-analyzer spotify-playlist-analyzer`
2. Right click a playlist in spotify
3. Select cShare``
4. Select `Copy Spotify URI`
5. Example:
```

https://open.spotify.com/playlist/603oF0bPdW4ZwSCHF8Zs4L

```
6. Paste the copied URI into the command window
7. Press Enter
```
