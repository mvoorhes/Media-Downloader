import pytube
from pytube import YouTube
from ffmpy import FFmpeg
import os
import constants as cs

OPATH = 'Videos'

def Download(link, type, quality='720p', opath=OPATH):
    try:
        video = YouTube(link)
        vidname = video.title
    except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable):
        print("ERROR: Invalid Link")
        return cs.error_types.INVALID_LINK
    
    try:
        if type == cs.download_type.mp3.value:
            stream = video.streams.get_highest_resolution()
        else:
            stream = video.streams.filter(res=quality).first()
    except pytube.exceptions.AgeRestrictedError:
        print("ERROR: Blocked from accessing this video")
        return cs.error_types.VIDEO_BLOCKED


    if stream is None:
        if quality == '1440p' or quality == '2160p':
            # Resolution is just too high; get highest
            print("Resolution is too high; Getting next best res")
            stream = video.streams.get_highest_resolution()
        else:
            # Find next best resolution from options list
            print("Resolution is unavailable; getting next best resolution")
            quality = cs.options[cs.options.index(quality) + 1] # Gets next resolution
            print(quality)
            stream = video.streams.filter(res=quality).first()


    try:
        stream.download(output_path=opath, filename=vidname+'.mp4')
    except:
        print("ERROR: Cannot download this video")
        return cs.error_types.BAD_STREAM
 
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


    return cs.error_types.SUCCESS