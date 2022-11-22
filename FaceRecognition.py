import PySimpleGUI as sg
import cv2
video = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
format = [[sg.Image(key = "image")],[sg.Text("People in Picture: 0", key = "text", expand_x = True, justification = "centre")]]
window = sg.Window("Face Detector", format)
while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
    check, frame = video.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayFrame, scaleFactor = 1.3, minNeighbors = 7)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    imgbytes = cv2.imencode(".png", frame)[1].tobytes()
    window["image"].update(data = imgbytes)
    numInFrame = "People in Picture: " + str(len(faces))
    window["text"].update(numInFrame)
window.close()
