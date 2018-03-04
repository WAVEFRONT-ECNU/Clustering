# The main file of module "Clustering"

from Clustering.config import configs  # The config file.
import Clustering.audio_class
import Clustering.import_file
import Clustering.cluster_kmeans
import librosa
import numpy as np

filelist = []
people_number = 2
__audiolist = []


def start_culster():
    n_mfcc = configs['n_mfcc']
    frame_size = configs['frame_size']
    frame_shift = configs['frame_shift']
    r = range(0, len(filelist))
    for i in r:
        audio = audio_class.audio()
        audio.filename = filelist[i][0]
        audio.filepath = filelist[i][1]
        y, audio.sr, audio.d = import_file.load_audio_file(audio.filepath)
        mfccs = librosa.feature.mfcc(y, audio.sr, n_mfcc=n_mfcc, hop_length=frame_shift, n_fft=frame_size)
        audio.mfccs_average = np.mean(mfccs[1:40], axis=1)
        __audiolist.append(audio)

    audiolist = cluster_kmeans.cluster(__audiolist, people_number)
    peoplelist = []
    for i in r:
        p = [audiolist[i].filename, audiolist[i].people]
        peoplelist.append(p)
    return peoplelist
