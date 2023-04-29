import instagrapi
import spotipy
from spotipy.oauth2 import SpotifyOAuth
cl = instagrapi.Client()
import requests
import os #only for env variable
import time


from pprint import pprint


from instagrapi.exceptions import LoginRequired


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ACCESS_TOKEN = "filler"
REFRESH_TOKEN = "YOUR_REFRESH_TOKEN"

token_info = {'access_token': ACCESS_TOKEN, 'expires_at': 1668837043, 'expires_in': 3600, 'refresh_token': REFRESH_TOKEN, 'scope': 'user-read-currently-playing', 'token_type': 'Bearer'}
def get_current_track():
    global token_info
    # Checking if token has expired
    now = int(time.time())
    is_token_expired = token_info.get('expires_at') - now < 60


    if (is_token_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info.get('refresh_token'))

    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {token_info.get('access_token')}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]
    playback = json_resp["is_playing"]
    prog = json_resp["progress_ms"]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link,
    	"playback":playback,
        "progress" : prog
    }

    return current_track_info

def format_time(ms):
    seconds = ms//1000
    return str(seconds//60)+":"+str(seconds%60)

def main():
    current_track_id = None
    playback_states = {True:"Ⅱ",False:"►"}
    while True:
        print("program now running")
        current_track_info = get_current_track()

        if current_track_info['id'] != current_track_id:

            current_playback_id = current_track_info["playback"]
            time_passed = format_time(current_track_info["progress"])
            #song_length = str((int(current_track_info["duration"]) % 1000) // 60) + ":" + str((int(current_track_info["duration"]) % 1000) % 60)
            song_length = "??"

            artists = current_track_info["artists"]
            song = current_track_info["track_name"]
            if "," in current_track_info["artists"]:
                artists = artists.split(",")[0]
            if len(f'[Now playing:{current_track_info["track_name"]}]\n [By: {artists}]') > 149:
                song = "2long4bio"


            time.sleep(5)
            pprint(current_track_info,indent=4)
            print("Updated bio is now : \n")
            print(f'"Privacy is an invention and we have lost it"\n [Now playing:{song}]\n [By: {artists}]')

            #cl.account_set_biography(f'"Privacy is an invention and we have lost it"\n [Now playing:{song}]\n [By: {artists}]')
            cl.account_set_biography(f"Now Playing:\n.\n        [{song}]-[{artists}]\n{time_passed}  ❍─────── {song_length}\n       ↻   ◃◃  {playback_states[current_playback_id]}  ▹▹     ↺")
            current_track_id = current_track_info['id']

        time.sleep(43.5)
        current_track_info = get_current_track()
        if current_playback_id != current_track_info["playback"]:
            current_playback_id = current_track_info["playback"]
            #time_passed = str((int(current_track_info["progress"]) % 1000) // 60) + ":" + str((int(current_track_info["progress"]) % 1000) % 60)
            time_passed = format_time(current_track_info["progress"])
            print("bio is now: \n")
            print(f"Now Playing:\n.\n        [{song}]-[{artists}]\n{time_passed}  ❍─────── {song_length}\n       ↻   ◃◃  {playback_states[current_playback_id]}  ▹▹     ↺")
            cl.account_set_biography(f"Now Playing:\n.\n        [{song}]-[{artists}]\n{time_passed}  ❍─────── {song_length}\n       ↻   ◃◃  {playback_states[current_playback_id]}  ▹▹     ↺")
            
            #put thing here
        else:
            time_passed = format_time(current_track_info["progress"])
            print("bio is now: \n")
            print(f"Now Playing:\n.\n        [{song}]-[{artists}]\n{time_passed}  ❍─────── {song_length}\n       ↻   ◃◃  {playback_states[current_playback_id]}  ▹▹     ↺")
            cl.account_set_biography(f"Now Playing:\n.\n        [{song}]-[{artists}]\n{time_passed}  ❍─────── {song_length}\n       ↻   ◃◃  {playback_states[current_playback_id]}  ▹▹     ↺")




cl.load_settings('session.json')

#it does not use this if session.json is loaded
cl.login("user", "password")


def create_spotify_oauth():
    return SpotifyOAuth(
            client_id="FILL-ME",
            client_secret="FILL-ME",
            redirect_uri="http://192.168.12.66:81/authorize",
            scope="user-read-currently-playing")

if __name__ == '__main__':
    try:
        main()
    except:
        time.sleep(300)
        main()