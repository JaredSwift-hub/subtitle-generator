from moviepy.editor import *

def split_audio_video(path,title):
    video = VideoFileClip(path)
    audio = video.audio
    path = '../audio/'+title+'.wav'
    audio.write_audiofile(path)
    return path

