from pytube import YouTube
from ffmpy import FFmpeg
import os

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

    # if type == 'mp3':
    #     # Quality is likely not a concern when downloading mp3, get highest
    #     video = video.streams.get_highest_resolution()
    # else:
    #     video = video.streams.filter(res=quality).first()
    #     # video = video.streams.get_highest_resolution()
 
    try:
        video.download(output_path=opath, filename=vidname+'.mp4')
    except:
        print("ERROR: Failed to download video")
        return False
 
    # Since we can't download audio only in mp3 format,
    # we convert to mp3 using ffmpeg.
    # This also reduces file size dramatically.
    if type != 'mp4':
    
        IN_FILE = opath + '/' + vidname + '.mp4'
        OUT_FILE = opath + '/' + vidname + '.mp3'
    
        ff = FFmpeg(
            inputs = {IN_FILE: None},
            outputs = {OUT_FILE: None}
        )
        
        ff.run()
        
        try:
            os.remove(IN_FILE)
        except:
            print("ERROR: Could not remove video portion")


    return True