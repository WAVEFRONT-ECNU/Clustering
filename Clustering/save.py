# import librosa
import shutil

def save_wav_in_group(audiolist,filelist): #(raw_y, sr, segpoint, path: str, name: str, startnum=0):
    # segpoint = []
    # for sp in segpointtime:
    # segpoint.append(int(sp * sr))
    # rangeloop = range(len(audiolist))
    for i in len(audiolist):
        for j in len(audiolist[i]):
            filename=audiolist[i][j].filename
            savepath=audiolist[i][j].filepath[:-filename.length] + "group/" + i + "/" +filename
            shutil.copyfile(filelist[i][1],savepath)
    return