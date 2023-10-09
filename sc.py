from sclib import SoundcloudAPI, Track, Playlist
import constants as cs
import os

# Source for a lot of this code
# https://pypi.org/project/soundcloud-lib/

def download_playlist(playlist, output_path):
    output_path += "/"
    output_path = os.path.join(output_path, playlist.title)
    os.mkdir(output_path)
    flag = cs.error_types.SUCCESS
    for track in playlist.tracks:
        if download_track(track, output_path) == cs.error_types.UNKNOWN:
            flag = cs.error_types.PLAYLIST_INCOMPLETE   # continue downloading with incomplete playlist
            continue
    return flag

def download_track(track, output_path):
    try:
        filename = f'./{track.artist} - {track.title}.mp3'
        destination = output_path + '/' + filename

        with open(destination, 'wb+') as file:
            track.write_mp3_to(file)
    except:
        print("ERROR: Could not download track")
        return cs.error_types.UNKNOWN

    return cs.error_types.SUCCESS

def download(name, output_path=cs.OPATH):
    api = SoundcloudAPI()
    link = api.resolve(name)
    if type(link) is Track:
        download_track(link, output_path)
    elif type(link) is Playlist:
        download_playlist(link, output_path)
    else:
        return cs.error_types.INVALID_LINK

    return cs.error_types.SUCCESS

