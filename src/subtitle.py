# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:07:08 2020

@author: jared
"""
from speech_to_text import speech_to_text
from split_audio_video import split_audio_video
#from split import split
from make_audio_chunks import make_audio_chunks
import os
import sys
import wave
import contextlib
import ntpath
class subtitle_line:
    def __init__(self, sequence_num, text, start_time, end_time):
        self.sequence_num = sequence_num
        self.text = text
        self.start_time = start_time
        self.end_time = end_time

class subtitles:
    def __init__(self, title):
        self.title = title
        self.subs = []
        
def format_time(seconds):
    seconds = seconds % (24*3600)
    hour = seconds // 3600
    seconds%= 3600
    minutes = seconds // 60
    seconds%=60
    return "%02d:%02d:%02d,000" % (hour, minutes, seconds)

def duration(audio_path):
    with contextlib.closing(wave.open(audio_path, 'r')) as f:
        frame_count = f.getnframes()
        fps = f.getframerate()
        return frame_count/float(fps)

def export(_subtitles):
    title = _subtitles.title
    f = open('../subs/'+title+'.srt', 'a')
    for sub in _subtitles.subs:
        print ('{}{}'.format(sub.start_time, sub.end_time))

        f.write(str(sub.sequence_num)+ '\n')
        start = format_time(sub.start_time)
        end = format_time(sub.end_time)
        f.write(start + ' --> ' + end + '\n')
        f.write(sub.text)
        f.write('\n\n')
    f.close()
    return 1

def convert(language):
    return 1

def main():
    #get file
    path = sys.argv[1]
    #language = sys.argv[2]
    print('Video path: {}'.format(path))
    title = ntpath.basename(path)
    title = os.path.splitext(title)[0]
    print('Video title: {}'.format(title))
    Subtitles = subtitles(title)
    #if language:
    #    print('not implemented')
    print('Separating audio from video')
    audio_path = split_audio_video(path,title)
    dur = duration(audio_path)
    print('Video length: {}s'.format(dur))
 #   inc = 0
 #   x=0
 #   while x <= dur:
 #       split(audio_path, x, x+15, inc, title)
 #       inc+=1
 #       x+=15        
 #
    print('Getting audio chunks')
    inc = make_audio_chunks(audio_path, title)
    print('Generating subtitles')
    for i in range(0, inc-1):
        text = speech_to_text('../audio/'+title+'-'+str(i+1)+'.wav')   
        print('Generate subtitles for sequence {} of {} for {}'.format(i+1, inc, title))    
        sub = subtitle_line(i+1, text, i*15, (i*15)+15)
        Subtitles.subs.append(sub)
    print('All subtitles generated')
    print('Exporting')    
    export(Subtitles)



if __name__=='__main__':
    
    main()
    
    
    
    
#1. Take video filename, and arg for language (Default is English)
#2. Play the video, and use speech synthesis to create a list of subtitle_line classes
#3. Export list to .srt file
#4.  Run video with subs 
