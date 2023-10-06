from pytube import YouTube
from ffmpy import FFmpeg
import os
import constants as cs

OPATH = 'Videos'

def Download(link, type, quality=1, opath=OPATH):
    video = YouTube(link)
    vidname = video.title
    print(video.thumbnail_url)
    
    try:
        video = video.streams.get_highest_resolution()
    except:
        print("ERROR: Cannot Access Video")
        return False
 
    try:
        video.download(output_path=opath, filename=vidname+'.mp4')
    except:
        print("ERROR: Failed to download video")
        return False
 
    # Since we can't download audio only in mp3 format,
    # we convert to mp3 using ffmpeg.
    # This also reduces file size dramatically.
    if type != cs.download_type.mp4.value:
        IN_FILE = opath + '/' + vidname + '.mp4'
        OUT_FILE = opath + '/' + vidname + '.mp3'
        ff = FFmpeg(
            inputs = {IN_FILE: None},
            outputs = {OUT_FILE: None}
        )        
        ff.run()
        os.remove(IN_FILE)


    return True