import spotipy
import spotipy.util as util
import os
import sys
from dotenv import load_dotenv
import argparse

# Searches for a file with .env make sure its set with the values from .example-env
load_dotenv()


token = ''

def get_help():
    """
    Returns the help message.
    """
    return """
        This program is to change to a different song on spotify via the terminal.

        Use it like this

        python app.py name of your track

        example usage:

        python app.py Master of Puppets
        """

def get_username():
    return os.getenv('USERNAME')

def get_token():
    global token
    if not token:
        scope = 'user-read-playback-state user-modify-playback-state'

        token = util.prompt_for_user_token(
            get_username(), 
            scope, 
            client_id=os.getenv('CLIENT_ID').strip(),
            client_secret=os.getenv('CLIENT_SECRET').strip(),
            redirect_uri='http://127.0.0.1:8080'
        )

    if token:
        return token
    else: 
        raise Exception('Could not get user-token. Make you set them in the .env file')


def get_spotify_client():
    return spotipy.Spotify(auth=get_token())


def retrive_song_from_input():
    """
    @return str. returns the user input that he sended as a argument. 
    """
    # sp = spotipy.Spotify(auth=get_token())
    try:
        return str(sys.argv[1:])
    except:
        # TODO replace with help options
        exit()

def get_song_uri(track_name:str):
    """
    Searches on spotify for trackname and retrives its uri.
    @param track_name The name of the track you wish to retive the uri from. 
    @return str. The song uri coming from spotify. 
    """
    sp = get_spotify_client()
    track_result = sp.search(q=track_name, type='track', limit=1)

    try:
        return track_result["tracks"]["items"][0]["uri"]
    except:
        # TODO add helpfull error message maybe with i3 message.
        print("Could not find the specified track")
        exit()


def get_get_active_device_id():
    """
    @return str. The id of the spotify client device that is currently active. 
    """
    sp = get_spotify_client()
    devices = sp.devices()["devices"]
    try:
        active_devices = list(filter(lambda device: device["is_active"], devices))
        return active_devices[0]["id"]
    except:
        print("Could not get devices")
        exit()

def set_active_song(track_spotify_uri:str, device_id:str):
    """
    Sets the current active song on a given device.
    @return bool. If there was a succes. 
    """
    sp = get_spotify_client()
    try:
        sp.start_playback(
            uris=[track_spotify_uri], 
            offset={
                "position": 0
            }, 
            device_id=device_id
        )
        return True
    except:
        return False

def main():
        user_input = retrive_song_from_input()
        if user_input:
            track_uri = get_song_uri(user_input)

            active_device_id = get_get_active_device_id()

            set_active_song(track_uri, active_device_id)
        else:
            print("No trackname provided. This is the help mesage to get you in the right direction")
            print(get_help)

if __name__ == '__main__':
    main()