import requests
import json

def get_youtube_id(song_name):
    song_name = song_name.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={song_name}"
    response = requests.get(url)
    search_results = response.text
    start = search_results.find("videoId") + 10
    end = start + 11
    youtube_id = search_results[start:end]
    return youtube_id

print(get_youtube_id("Shape of You"))

songs = [
    {"artist": "Devo", "song": "Whip It"},
    {"artist": "The Clash", "song": "Should I Stay or Should I Go"},
    {"artist": "The B-52s", "song": "Love Shack"},
    {"artist": "Gary Numan", "song": "Cars"},
    {"artist": "Joy Division", "song": "Love Will Tear Us Apart"},
    {"artist": "Talking Heads", "song": "Once in a Lifetime"},
    {"artist": "New Order", "song": "Blue Monday"},
    {"artist": "Blondie", "song": "Heart of Glass"},
    {"artist": "The Stranglers", "song": "Golden Brown"},
    {"artist": "The Go-Go's", "song": "We Got the Beat"}
]
print(songs)

import os
import youtube_dl

def download_songs(songs):
    for song in songs:
        artist = song['artist']
        song_name = song['song']
        youtube_id = get_youtube_id(artist + " " + song_name) 
        ydl_opts = {'outtmpl': '%(artist)s - %(title)s.%(ext)s'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['http://www.youtube.com/watch?v=' + youtube_id])

download_songs(songs)

