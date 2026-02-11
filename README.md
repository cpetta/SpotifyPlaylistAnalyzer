# SpotifyPlaylistAnalyzer

## Important Status Update
As of March 9 2026, this program will no longer work due to changes to the Spotify API.

Please see this
<a href="https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security" target="_blank">Spotify blog post on this change</a>
and
<a href="https://developer.spotify.com/documentation/web-api/references/changes/february-2026" target="_blank">Spotify API change log</a>

## Requirements

- Docker CLI
- Spotify API Keys

## Setup

1. Obtain a spotify Client ID and Client Secret ID from `https://developer.spotify.com/dashboard`
2. Add the Spotify Client ID to `src/api_keys/spotify_client_id.txt`
3. Add the Spotify Client Secret ID to `/src/api_keys/spotify_client_secret.txt`
4. Run the below docker build command from the command lind

```
docker build -t spotify-playlist-analyzer .
```

## Usage

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
8. Example output

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
1 - Emancipator
2 - RJD2
3 - Little People
4 - Bonobo
5 - The Glitch Mob
6 - Blockhead
7 - Ancient Astronauts
8 - Prefuse 73
9 - Aydio
10 - Trifonic
```
