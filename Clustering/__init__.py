# The main file of module "Clustering"

from Clustering.config import configs  # The config file.
import Clustering.audio_class
import Clustering.import_file
import librosa

filelist = []
__audiolist = []


def start_culster():
    n_mfcc = configs['n_mfcc']
    frame_size = configs['frame_size']
    frame_shift = configs['frame_shift']
    r = range(0, len(filelist))
    for i in r:
        audio = audio_class.audio()
        audio.filename = filelist[i][0]
        y, audio.sr, audio.d = import_file.load_audio_file(filelist[i][1])
        audio.mfccs = librosa.feature.mfcc(y, audio.sr, n_mfcc=n_mfcc, hop_length=frame_shift, n_fft=frame_size)
        __audiolist.append(audio)
