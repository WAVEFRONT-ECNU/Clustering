# The main file of module "Clustering"

from Clustering.config import configs  # The config file.
import Clustering.audio_class
import Clustering.import_file
import numpy as np

__filelist = []
__audiolist = []


def load_file_list(filelist):
    __filelist = filelist


def start_culster():
    r = range(0, len(__filelist))
    for i in r:
        audio = audio_class.audio()
        audio.filename = __filelist[i][0]
        audio.audio_content, audio.sr, audio.d = import_file.load_audio_file(__filelist[i][1])
        __audiolist.append(audio)
