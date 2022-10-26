def button_clicked():
    global heightlbl
    height = entry.get()
    heightlbl.delete(0,tk.END)
    heightlbl.insert("0",height)
def reset():
    global entry, heightlbl
    heightlbl.delete(0,tk.END)
    entry.delete(0,tk.END)

import tkinter as tk
window = tk.Tk()
window.geometry("400x200")
window.config(bg="#45f7e0")
frame = tk.Label(bg="#45f7e0")
label = tk.Label(text = "Please enter your height in cm:", bg = "#40edd8")
entry = tk.Entry()
button = tk.Button(text = "Done.", command = button_clicked, bg = "#40edd8")
button2 = tk.Button(text = "Reset.", command = reset, bg = "#40edd8")
heightlbl = tk.Entry()
label.pack()
entry.pack()
button.pack()
frame.pack()
button2.pack()
heightlbl.pack()
