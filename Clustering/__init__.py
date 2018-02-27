# The main file of module "Clustering"

from Clustering.config import configs  # The config file.
import Clustering.audio_class
import Clustering.import_file
import Clustering.cluster_kmeans
import librosa

filelist = []
__audiolist = []


def start_culster():
    n_mfcc = configs['n_mfcc']
    frame_size = configs['frame_size']
    frame_shift = configs['frame_shift']
    mfcc_list = []
    r = range(0, len(filelist))
    for i in r:
        audio = audio_class.audio()
        audio.filename = filelist[i][0]
        audio.filepath = filelist[i][1]
        y, audio.sr, audio.d = import_file.load_audio_file(audio.filepath)
        audio.mfccs = librosa.feature.mfcc(y, audio.sr, n_mfcc=n_mfcc, hop_length=frame_shift, n_fft=frame_size)
        r = range(0, len(audio.mfccs))
        mfcc = []
        for i in r:
            m = audio.mfccs[i]
            ma = sum(m) / len(m)
            mfcc.append(ma)
        audio.mfcc_average = mfcc
        mfcc_list.append(audio.mfcc_average)
        __audiolist.append(audio)

    assignments = cluster_kmeans.cluster_kmeans(mfcc_list, configs['people_num_test'])
    # TODO finish cluster output
    audiolist = []
    for au in __audiolist:
        aud = [au.filename, au.people]
        audiolist.append(aud)
    return audiolist
