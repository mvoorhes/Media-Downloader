from enum import Enum

OPATH = ''
BACKGROUND = 'blue'
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
    YOUTUBE = 1
    SOUNDCLOUD = 2

class download_type(Enum):
    MP3 = 1
    MP4 = 2