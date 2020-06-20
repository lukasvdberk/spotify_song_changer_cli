import spotipy
import spotipy.util as util
import os
import sys



def get_username():
    return os.getenv('USERNAME')

def get_token():
    global token
    if not token:
        scope = 'playlist-read-private'

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

def retrive_song_from_input():
    """
    @return str. returns the user input that he sended as a argument. 
    """
    # sp = spotipy.Spotify(auth=get_token())
    try:
        return str(sys.argv[1])
    except:
        # TODO replace with help options
        exit()

def get_song_uri(track_name:str):
    """
    Searches on spotify for trackname and retrives its uri.
    @param track_name The name of the track you wish to retive the uri from. 
    @return str. The song uri coming from spotify. 
    """
    pass


def get_get_active_device_id():
    """
    @return str. The id of the spotify client device that is currently active. 
    """
    pass

def set_active_song(track_spotify_uri:str, device_id:str):
    """
    Sets the current active song on a given device.
    @return str. The id of the spotify client device that is currently active. 
    """
    pass


def main():
        # FLOW
        # reads input
        # searches for songs on spotify
        # searches for available devices
        # play song on active client
        user_input = retrive_song_from_input()
if __name__ == '__main__':
    main()