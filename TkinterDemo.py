import tkinter as tk
window = tk.Tk()
button = tk.Button(text = "Click me!", fg = "black", bg = "white", width = 10, height = 1)
button.pack()
message = tk.Label(text = "Email Address:", fg = "black", bg = "white", width = 10, height = 1)
message.pack()
entry = tk.Entry(fg = "black", bg = "white", width = 50)
entry.pack()
textBox = tk.Text()
textBox.pack()
#.get().delete(eg.0,4 or tk.END).insert(canshifttext eg. 0,"hi")
#fortextBox.get("1.0","1.5")requireslinenumber(starts1)andcharacterposition(starts0)
#togetwholemessageuse.get("1.0",tk.END)
email = entry.get()
window.mainloop()
#Frame()takeupspaceinwidget:flat/sunken/raised/groove/ridge
#Label-lbl/Button-btn/Entry-ent/Text-txt/Frame-frm

