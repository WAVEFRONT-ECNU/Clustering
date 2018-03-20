import WaveSlicer
import Clustering
import os
import multiprocessing


def fileDemo():
    raw = input("\nInput raw file name:")
    WaveSlicer.cut_audio_fromfile(raw, sp="output/", sn="test")


def streamDemo():
    p = multiprocessing.Process(target=WaveSlicer.cut_audio_fromstream("output/", "1"))
    p.start()
    stopFlag = input("\nInput Any Key To Stop...\n")
    if stopFlag != "":
        p.terminate()


def readAudioList():
    path = "output/"
    audiolist = []
    for maindir, subdir, file_name_list in os.walk(path):
        for filename in file_name_list:
            apath = [filename, path + filename]
            audiolist.append(apath)
    return audiolist


def clusterDemo(audiolist,peoplenumber):
    Clustering.people_number = peoplenumber
    Clustering.filelist = audiolist
    outlist = Clustering.start_culster()
    print(outlist)

if __name__ == "__main__":
    print("Choose mode: \n1.From File \n2.From Stream \n")
    mode = input()
    if not os.path.exists("output/"):
        os.mkdir("output/")
    if mode == "1":
        fileDemo()
    elif mode == "2":
        streamDemo()
    peoplenumber = input("\nPlease input people number:\n")
    audiolist = readAudioList()
    clusterDemo(audiolist,peoplenumber)
