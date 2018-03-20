import WaveSlicer
import Clustering
import time
import os


def fileDemo():
    raw = input("Input raw file name:")
    WaveSlicer.cut_audio_fromfile(raw, sp="output/", sn="test")


def streamDemo():
    WaveSlicer.cut_audio_fromstream("output/", "1")


def readAudioList():
    path = "output/"
    audiolist = []
    for maindir, subdir, file_name_list in os.walk(path):
        for filename in file_name_list:
            apath = [filename, path + filename]
            audiolist.append(apath)
    return audiolist


def clusterDemo(audiolist):
    start = time.time()
    Clustering.people_number = 2
    Clustering.filelist = audiolist
    outlist = Clustering.start_culster()
    print(outlist)
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    print("Choose mode: \n1.From File \n2.From Stream \n")
    mode = input()
    if mode == "1":
        fileDemo()
    elif mode == "2":
        streamDemo()
    audiolist = readAudioList()
    clusterDemo(audiolist)
