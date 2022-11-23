import PySimpleGUI as sg
layout = [[sg.Text("What's your name?")],
          [sg.Input(key = "input")],
          [sg.Text(size = (40,1), key = "output")],
          [sg.Button("Ok"), sg.Button("Exit")]]
window = sg.Window("Introduction", layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    window["output"].update("Hi " + values["input"] + "!")
window.close()
