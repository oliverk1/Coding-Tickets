def buttonClicked():
    distance = entry.get()
    validDistance(distance)

def reset():
    textbox.delete(1.0, tk.END)
    entry.delete(0, tk.END)

def validDistance(distance):
    try:
        distance=float(distance)
    except ValueError:
        textbox.delete(1.0, tk.END)
        textbox.insert(1.0, "ERROR")
    else:
        fare(distance)

def fare(distance):
    fare = 2.8 + (1.5 * distance)
    fare = round(fare, 2)
    textbox.delete(1.0, tk.END)
    textbox.insert(1.0, "£")
    textbox.insert(tk.END, fare)

def main():
    global entry, textbox
    window = tk.Tk()
    window.geometry("450x315")
    window.config(bg="yellow")
    title = tk.Label(text = "Taxi Fare Calculator.", bg = "black", fg = "yellow")
    title.config(font=('Helvetica bold', 26))
    space = tk.Label(bg = "yellow")
    label = tk.Label(text = "Enter distance in km:", bg = "black", fg = "yellow")
    label.config(font=('Helvetica bold', 15))
    entry = tk.Entry(bg = "black", fg = "yellow", width = "6")
    entry.config(font=('Helvetica bold', 20))
    space2 = tk.Label(bg = "yellow")
    donebtn = tk.Button(text = "Done.", command = buttonClicked, bg = "black", fg = "yellow")
    donebtn.config(font=('Helvetica bold', 12))
    space3 = tk.Label(bg = "yellow")
    resetbtn = tk.Button(text = "Reset.", command = reset, bg = "black", fg = "yellow")
    resetbtn.config(font=('Helvetica bold', 12))
    space4 = tk.Label(bg = "yellow")
    textbox = tk.Text(bg = "black", fg = "yellow", height = "1", width = "6")
    textbox.config(font=('Helvetica bold', 20))
    title.pack()
    space.pack()
    label.pack()
    entry.pack()
    space2.pack()
    donebtn.pack()
    space3.pack()
    resetbtn.pack()
    space4.pack()
    textbox.pack()
    
import tkinter as tk
main()

