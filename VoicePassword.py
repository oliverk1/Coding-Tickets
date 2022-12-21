def GetPassword():
    message = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say the password or exit...")
        audio = r.listen(source)
        try:
            message = str(r.recognize_google(audio))
        except Exception as e:
            print("Error: " + str(e))
    return message

def unlock(password):
    if password == "hello there general Kenobi":
        print("Password Accepted")
        lock = 0
    else:
        lock = 1
    return lock

def main():
    lock = 1
    while lock == 1:
        password = GetPassword()
        lock = unlock(password)
        if password == "exit":
            break

import speech_recognition as sr
main()