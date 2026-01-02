import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)

    try:
        return r.recognize_google(audio).lower()
    except:
        return None