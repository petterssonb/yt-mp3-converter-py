import ssl
import tkinter
import customtkinter
from yt_dlp import YoutubeDL
from pathlib import Path
import re
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from fuzzywuzzy import fuzz

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

local_files_dir = str(Path.home() / "Music/SpotifyLocalFiles")
downloaded_song_title = None
spotify_song_found = False
spotify_track_id = None

def extract_artist_and_title(title):
    title = re.sub(r'[\(\[].*?[\)\]]', '', title)
    title = re.sub(r'[-]', '', title)
    title = re.sub(r'\b(official|audio|video|lyrics|explicit|remastered|full|hd|mv|music)\b', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s+', ' ', title).strip()

    if '-' in title:
        artist, song_title = [part.strip() for part in title.split('-', 1)]
    else:
        artist, song_title = title.split(' ', 1)

    return artist.title(), song_title.title()

def search_spotify_artist_and_song(song_title):
    global spotify_song_found
    global spotify_track_id

    if 'sp' not in globals() or sp is None:
        connect_spotify()

    artist, song_title = extract_artist_and_title(song_title)
    artist_results = sp.search(q=f'artist:{artist}', type='artist', limit=1)

    if not artist_results['artists']['items']:
        spotify_song_found = False
        return None

    track_results = sp.search(q=f'artist:{artist} track:{song_title}', type='track', limit=5)

    for track in track_results['tracks']['items']:
        track_name = track['name']
        track_artist = track['artists'][0]['name']

        similarity = fuzz.ratio(song_title, track_name)

        if similarity >= 80:
            spotify_track_id = track['id']
            spotify_song_found = True
            return track['id']

    spotify_song_found = False
    return None

def startDownload():
    global downloaded_song_title
    global spotify_song_found
    global spotify_track_id
    ytLink = link.get()
    ssl._create_default_https_context = ssl._create_unverified_context

    try:
        finishLabel.configure(text="Downloading MP3...", text_color="orange")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(Path(local_files_dir) / "%(title)s.%(ext)s"),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [on_progress_hook],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(ytLink, download=True)
            downloaded_song_title = info_dict['title']
            
            finishLabel.configure(text=f"Downloaded and saved to Local Files: {downloaded_song_title}.mp3", text_color="orange")
        
        spotify_track_id = search_spotify_artist_and_song(downloaded_song_title)

        if spotify_track_id:
            finishLabel.configure(text=f"Song found on Spotify: {downloaded_song_title}", text_color="green")
            spotify_song_found = True
        else:
            finishLabel.configure(text=f"Song not found on Spotify: {downloaded_song_title}", text_color="orange")
            finishLabelSecond.configure(text="This song is only available in local files. Check your Spotify 'Local Files'.", text_color="orange")
    
    except Exception as e:
        finishLabel.configure(text="Error downloading video", text_color="red")


def on_progress_hook(d):
    if d['status'] == 'downloading':
        percent_str = re.sub(r'\x1b\[[0-9;]*m', '', d['_percent_str']).strip()
        pPercentage.configure(text=f"{percent_str}")
        pPercentage.update()

        try:
            progressBar.set(float(percent_str.strip('%')) / 100)
        except ValueError:
            pass

def connect_spotify():
    global sp
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private playlist-modify-public"
    ))

    spotifyStatusLabel.configure(text="Connected to Spotify!", text_color="green")
    spotifyStatusLabel.pack(padx=10, pady=10)
    load_playlists()

def load_playlists():
    try:
        playlists = sp.current_user_playlists()
        playlist_names = [playlist['name'] for playlist in playlists['items']]

        if not playlist_names:
            finishLabel.configure(text="No playlists found.", text_color="red")
            return

        playlistMenu.set(playlist_names[0])
        playlistMenu.configure(values=playlist_names, state="normal")
    except Exception as e:
        finishLabel.configure(text=f"Error loading playlists: {str(e)}", text_color="red")

def add_to_spotify():
    global downloaded_song_title
    global spotify_song_found
    global spotify_track_id

    if not downloaded_song_title:
        finishLabel.configure(text="No song downloaded or identified. Please download or select a song first.", text_color="red")
        return

    if spotify_song_found and spotify_track_id:
        if spotify_track_id:
            playlist_id = None
            playlists = sp.current_user_playlists()
            for playlist in playlists['items']:
                if playlist['name'] == selected_playlist.get():
                    playlist_id = playlist['id']
                    break

            if playlist_id:
                sp.playlist_add_items(playlist_id, [spotify_track_id])
                finishLabel.configure(text=f"Song '{downloaded_song_title}' added to Spotify playlist!", text_color="green")
            else:
                finishLabel.configure(text="Playlist not found", text_color="red")
    else:
        finishLabel.configure(text=f"Follow the readme instructions on how to add '{downloaded_song_title}' to playlist", text_color="orange")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert Youtube URL")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabelSecond = customtkinter.CTkLabel(app, text="")
finishLabel.pack()
finishLabelSecond.pack()

pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

spotifyStatusLabel = customtkinter.CTkLabel(app, text="Not connected to Spotify", text_color="red")
spotifyStatusLabel.pack(padx=10, pady=10)

connectSpotifyButton = customtkinter.CTkButton(app, text="Connect to Spotify", command=connect_spotify)
connectSpotifyButton.pack(padx=10, pady=10)

selected_playlist = tkinter.StringVar()
playlistMenu = customtkinter.CTkOptionMenu(app, values=[], variable=selected_playlist, state="disabled")
playlistMenu.pack(padx=10, pady=10)

addToSpotifyButton = customtkinter.CTkButton(app, text="Add to Playlist", command=add_to_spotify)
addToSpotifyButton.pack(padx=10, pady=10)

app.mainloop()