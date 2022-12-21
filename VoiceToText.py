def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Talk...")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("Message: " + message)
        except Exception as e:
            print("Error: " + str(e))

import speech_recognition as sr
main()