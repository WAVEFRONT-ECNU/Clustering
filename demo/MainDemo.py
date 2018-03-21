import WaveSlicer
import Clustering
import os
import sys
import multiprocessing


def fileDemo():
    raw = input("\nInput raw file name:")
    WaveSlicer.cut_audio_fromfile(raw, sp="output/", sn="file")


def streamDemo():
    p = multiprocessing.Process(target=WaveSlicer.cut_audio_fromstream, args=("output/", "stream"))
    p.start()
    input("\nEnter To Stop...\n")
    p.terminate()


def readAudioList():
    path = "output/"
    audiolist = []
    for maindir, subdir, file_name_list in os.walk(path):
        for filename in file_name_list:
            apath = [filename, path + filename]
            audiolist.append(apath)
    return audiolist


def clusterDemo(audiolist, peoplenumber):
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
    audiolist = readAudioList()
    if len(audiolist) <= 1:
        print("Do not have enough voice fragment.")
        sys.exit(1)
    peoplenumber = input("\nPlease input people number:\n")
    while int(peoplenumber) <= 1:
        print("People number should be more than 2.")
        peoplenumber = input("\nPlease input people number:\n")
    clusterDemo(audiolist, peoplenumber)
    sys.exit(0)
