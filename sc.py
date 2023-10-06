from sclib import SoundcloudAPI, Track, Playlist

OPATH = 'Videos'

def download(name, output_path=OPATH):
    # do not pass a Soundcloud client ID that did not come from this library, but you can save a client_id that this lib found and reuse it
    api = SoundcloudAPI()
    try:
        track = api.resolve(name)
    except:
        print("ERROR: Could not resolve track")
        return False

    assert type(track) is Track

    try:
        filename = f'./{track.artist} - {track.title}.mp3'
        destination = output_path + '/' + filename

        with open(destination, 'wb+') as file:
            track.write_mp3_to(file)
    except:
        print("ERROR: Couldn't Download Track")
        return False

    return True

