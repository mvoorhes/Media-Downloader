from enum import Enum

OPATH = ''
BACKGROUND = 'blue'
WIDTH = 700
HEIGHT = 200
FONT = 'calibre'

options = [
    '144p', 
    '240p',
    '360p',
    '480p',
    '720p',
    '1080p',
    '1440p',
    '2160p'
]

class link_type(Enum):
    YouTube = 1
    Soundcloud = 2

class download_type(Enum):
    mp3 = 1
    mp4 = 2