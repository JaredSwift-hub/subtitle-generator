import speech_recognition
def speech_to_text(audio_path):
    recog = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(audio_path) as source:
        audio_text = recog.listen(source)
        try:
            text = recog.recognize_google(audio_text)
            return text
        except:
            print('err')