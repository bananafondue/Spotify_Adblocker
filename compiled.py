import time
import requests
from pycaw.pycaw import AudioUtilities                                         # To access windows volume mixer
from secrets import spotify_user_id, base_64, refresh_token

class Refresh:
    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64

    def refresh(self):                                                         # Funtion to refresh token,
        url = "https://accounts.spotify.com/api/token"                              # returns access token
        response = requests.post(
            url,
            data={
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            },
            headers={
                "Authorization": "Basic " + base_64
            }
        )
        response_json = response.json()
        return response_json["access_token"]

class SpotifyClient(object):

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.response = ""

    def call_refresh(self):                                                       # Calls refresh,
        print("Token refreshing")                                                 # updates the spotify_token variable
        refreshcaller = Refresh()                                                 # Proceeds to run function
        self.spotify_token = refreshcaller.refresh()
        self.run()

    def run(self):
        url = f"https://api.spotify.com/v1/me/player/currently-playing"

        self.response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.spotify_token}",
            }
        )

        if self.response.status_code == 400:
            print("token_expired")
            self.call_refresh()

        response_json = self.response.json()
        current_state = response_json['currently_playing_type']                   # Checks playing type,
        try:                                                                      # then calls muteit function
            if current_state == 'ad':
                muteit(True)
                print("spotify_muted")
            else:
                muteit(False)
                print("spotify unmuted")

        except TypeError:
            pass



def muteit(mute):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "Spotify.exe":
            if mute:
                volume.SetMute(1, None)
            else:
                volume.SetMute(0, None)


spotify_client = SpotifyClient()

while True:
    spotify_client.run()
    time.sleep(2)                                                                  # Checks every 2 seconds