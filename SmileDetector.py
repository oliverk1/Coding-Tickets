import PySimpleGUI as sg
import cv2
video = cv2.VideoCapture(0)
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
format = [[sg.Image(key = "image")]]
window = sg.Window("Smile Detector", format)
while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    check, frame = video.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    smile = smileCascade.detectMultiScale(grayFrame, scaleFactor = 1.3, minNeighbors = 35)
    face = faceCascade.detectMultiScale(grayFrame, scaleFactor = 1.3, minNeighbors = 15)
    if len(face) != 0:
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        for (x, y, w, h) in smile:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    imgbytes = cv2.imencode(".png", frame)[1].tobytes()
    window["image"].update(data = imgbytes)
window.close()
