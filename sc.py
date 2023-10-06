from sclib import SoundcloudAPI, Track, Playlist
import constants as cs
import os

# Source for a lot of this code
# https://pypi.org/project/soundcloud-lib/

def download_playlist(playlist, output_path):
    output_path += "/"
    output_path = os.path.join(output_path, playlist.title)
    os.mkdir(output_path)
    for track in playlist.tracks:
        if download_track(track, output_path) is False:
            return False
    return True

def download_track(track, output_path):
    try:
        filename = f'./{track.artist} - {track.title}.mp3'
        destination = output_path + '/' + filename

        with open(destination, 'wb+') as file:
            track.write_mp3_to(file)
    except:
        print("ERROR: Could not download track")
        return False

    return True

def download(name, output_path=cs.OPATH):
    api = SoundcloudAPI()
    link = api.resolve(name)
    if type(link) is Track:
        download_track(link, output_path)
    elif type(link) is Playlist:
        download_playlist(link, output_path)
    else:
        return False

    return True

