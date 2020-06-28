# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:07:08 2020

@author: jared
"""

class subtitle_line:
    def __init__(self, text, start_time, end_time):
        self.text = text
        self.start_time = start_time
        self.end_time = end_time


class subtitles:
    def __init__(self):
        self.subs = []
        

Subtitles = subtitles()


def play_video(video):
    return 1

def listen():
    return 1


def export():
    return 1

def convert(language):
    return 1

def test():
    return 1

def main():
    return 1

    
if __name__=='__main__':
    main()
    
    
    
    
#1. Take video filename, and arg for language (Default is English)
#2. Play the video, and use speech synthesis to create a list of subtitle_line classes
#3. Export list to .srt file
#4  Run video with subs 
