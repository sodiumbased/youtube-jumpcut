# make temp folder for mp4 and mp3
# use pytube3 to download low quality 144p video and convert; try pytube.Youtube('url here').streams.filter(only_audio=True).all()
# open audio file in audiotsm or pyAudio
# find video segments above certain preset threshold (maybe as a percentage of the max volume)
# document times and export srt file
# https://github.com/tyiannak/pyAudioAnalysis/wiki/5.-Segmentation

# test 1 for speech

from pyAudioAnalysis import audioBasicIO as aIO
from pyAudioAnalysis import audioSegmentation as aS
import os



# [Fs, x] = aIO.read_audio_file("mathswav.wav")
# segments = aS.silence_removal(x, Fs, 0.020, 0.020, smooth_window = 0.1, weight = 0.6, plot = False)
# print(segments)

#function for deciding to call it through a bash script
#set categories user can choose and add those weightings in a variable to send to the funciton

def silenceRemovalWrapper(inputFile, smoothingWindow, weight):
    soundTimes = open("soundOut" + inputFile + ".txt", "w")


    if not os.path.isfile(inputFile):   
        raise Exception("Input audio file not found!")

    [fs, x] = aIO.read_audio_file(inputFile)
    segmentLimits = aS.silence_removal(x, fs, 0.05, 0.05,
                                       smoothingWindow, weight, True)
    for i in segmentLimits:
        soundTimes.write(str(i) + '\n')
        # ', '.join(i)
    soundTimes.close()

silenceRemovalWrapper("maths.mp3", 0.1, 6)