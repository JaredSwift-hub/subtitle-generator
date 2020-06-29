from pydub import AudioSegment
from pydub.utils import make_chunks as mc


def make_audio_chunks(audio_path, title):
    sound = AudioSegment.from_file(audio_path, "wav")
    chunk_length_ms = 15000
    audio_chunks = mc(sound, chunk_length_ms)
    num_chunks=0
    for chunk_num, chunk in enumerate(audio_chunks):
        chunk_name = "../audio/{}-{}.wav".format(title, chunk_num+1)
        chunk.export(chunk_name, format = "wav")
        print('exporting{}'.format(chunk_name))
        num_chunks+=1
    return num_chunks
if __name__=='__main__':
    make_audio_chunks('../audio/GameofThrones.wav', 'GameofThrones')
    