def win(XO, event):
    if XO == "X":
        X.append(event)
        test = X
    else:
        O.append(event)
        test = O
    if "1" in test and "4" in test and "7" in test\
        or "2" in test and "5" in test and "8" in test\
        or "3" in test and "6" in test and "9" in test\
        or "1" in test and "2" in test and "3" in test\
        or "4" in test and "5" in test and "6" in test\
        or "7" in test and "8" in test and "9" in test\
        or "1" in test and "5" in test and "9" in test\
        or "3" in test and "5" in test and "7" in test:
        return True
    elif (len(X) + len(O)) == 9:
        return False

import PySimpleGUI as sg
X = []
O = []
layout = [[sg.Button("", size = 3, key = "1"), sg.Button("", size = 3, key = "2"), sg.Button("", size = 3, key = "3")],
          [sg.Button("", size = 3, key = "4"), sg.Button("", size = 3, key = "5"), sg.Button("", size = 3, key = "6")],
          [sg.Button("", size = 3, key = "7"), sg.Button("", size = 3, key = "8"), sg.Button("", size = 3, key = "9")],
          [sg.Text("", key = "text", expand_x = True, justification = "centre", visible = False), sg.Text("X's Turn", key = "text2", expand_x = True, justification = "centre")],
          [sg.Button("Restart", size = 6, key = "restart"), sg.Button("Quit", size = 6, key = "quit")]
          ]
sg.theme("darkblue")
window = sg.Window("Noughts and Crosses", layout)
count = 0
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "quit":
        break
    if event == "restart":
        for i in range(1, 10):
            i = str(i)
            window["text2"].update(visible = True)
            window[i].update("", disabled = False)
            window["text"].update("", visible = False)
            X = []
            O = []
            count = count + 1
    else:
        if (count % 2) == 0:
            window[event].update("X")
            window[event].update(disabled = True)
            w = win("X", event)
            winner = "X"
            window["text2"].update("O's Turn")
        else:
            window[event].update("O")
            window[event].update(disabled = True)
            w = win("O", event)
            winner = "O"
            window["text2"].update("X's Turn")
        if w == True:
            window["text2"].update(visible = False)
            window["text"].update(winner + " won!", visible = True)
            for i in range(1, 10):
                i = str(i)
                window[i].update(disabled = True)
        if w == False:
            window["text2"].update(visible = False)
            window["text"].update("Draw!", visible = True)
            for i in range(1, 10):
                i = str(i)
                window[i].update(disabled = True)
        count = count + 1
window.close()



