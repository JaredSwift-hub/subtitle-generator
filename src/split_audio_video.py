from moviepy.editor import *

def split_audio_video(path,title):
    video = VideoFileClip(path)
    audio = video.audio
    audio.write_audiofile('../audio/test')
    return '../audio/'+title

