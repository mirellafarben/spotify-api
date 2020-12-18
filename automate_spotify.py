# take songs from a noteblock
# create a playlist on spotify
# search spotify
# add to your playlist

import json
import requests
import getSongs
from datetime import date
from secrets import spotify_token, spotify_user_id


class CreatePlaylist:
    def __init__(self):
        self.spotify_token = spotify_token
        self.spotify_user_id = spotify_user_id
        self.song_uris = ""

    def create_playlist(self):
        print("don't mind me i'm just doin' stuff 👀")
        today = date.today()

        todayFormatted = today.strftime("%d/%m/%Y")

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)

        request_body = json.dumps({
            "name": todayFormatted + " automated playlist",
            "description": "Yes. I think I finaly did it.",
            "public": True
        })

        response = requests.post(query, data=request_body, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })

        response_json = response.json()
        print(response_json)
        return response_json["id"]

    def finds_songs(self):
        print("Finding songs...")

        for i in getSongs.get_songs():
            query = "https://api.spotify.com/v1/search?q={}&type=track".format(i)

            response = requests.get(query,
                                    headers={"Content-Type": "application/json",
                                             "Authorization": "Bearer {}".format(self.spotify_token)})

            response_json = response.json()
            # songs_string += (response_json["tracks"]["type"] + ",")
            # songs_string = songs_string[:-1]
            song_uri = response_json["tracks"]["items"][1]["uri"]
            self.song_uris += song_uri + ","
            print(i + song_uri)

        self.song_uris = self.song_uris[:-1]
        print(self.song_uris)

    def add_song_to_playlist(self):
        self.new_playlist_id = self.create_playlist()

        a.finds_songs()

        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
            self.new_playlist_id, self.song_uris)

        response = requests.post(query, headers={"Content-Type": "application/json",
                                                 "Authorization": "Bearer {}".format(self.spotify_token)})

        print(response.json)


a = CreatePlaylist()
a.add_song_to_playlist()
