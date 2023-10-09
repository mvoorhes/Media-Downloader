from enum import Enum

OPATH = 'Videos'    # Set this to whatever you want your default path to be
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

class error_types(Enum):
    SUCCESS = 1
    INVALID_LINK = -3
    VIDEO_BLOCKED = -1
    BAD_STREAM = -2
    PLAYLIST_INCOMPLETE = -4
    UNKNOWN = -5
    
