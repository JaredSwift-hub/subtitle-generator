from pydub import AudioSegment

def split(audio, start, end, inc,title):
    sound = AudioSegment.from_file(audio)
    segment = sound[start:end]
    segment.export('../audio/'+title+'-'+inc+'.wav', format='wav')