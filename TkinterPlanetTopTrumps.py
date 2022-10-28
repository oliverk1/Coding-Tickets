def GUI():
    global title, dfsent, sent, opent, noment
    window = tk.Tk()
    window.geometry("332x200")
    window.configure(bg = "black")
    title = tk.Entry(bg = "black", fg = "white")
    dfslbl = tk.Label(text = "Distance from Sun (10^6km):", bg = "black", fg = "white")
    dfsent = tk.Entry(bg = "black", fg = "white")
    slbl = tk.Label(text = "Size (Diameter km):", bg = "black", fg = "white")
    sent = tk.Entry(bg = "black", fg = "white")
    oplbl = tk.Label(text = "Orbital Period", bg = "black", fg = "white")
    opent = tk.Entry(bg = "black", fg = "white")
    nomlbl = tk.Label(text = "Number of Moons:", bg = "black", fg = "white")
    noment = tk.Entry(bg = "black", fg = "white")
    dfs = tk.Button(text = "Distance from Sun", bg = "black", fg = "white", command = dfsch)
    s = tk.Button(text = "Size", bg = "black", fg = "white", command = sch)
    op = tk.Button(text = "Orbital Period", bg = "black", fg = "white", command = opch)
    nom = tk.Button(text = "Number of Moons", bg = "black", fg = "white", command = nomch)
    title.pack()
    dfslbl.pack()
    dfsent.pack()
    slbl.pack()
    sent.pack()
    oplbl.pack()
    opent.pack()
    nomlbl.pack()
    noment.pack()
    dfs.pack(side="left")
    s.pack(side="left")
    op.pack(side="left")
    nom.pack(side="left")

def main():
    global Planets
    Planets = [["Mercury", 57.9, 4879, 88, 0],
        ["Venus", 108.2, 12104, 224.7, 0],
        ["Earth", 149.6, 12756, 365.2, 1],
        ["Mars", 227.9, 6792, 687, 2],
        ["Jupiter", 778.6, 142984, 4331, 67],
        ["Saturn", 1433.5, 120536, 10747, 64],
        ["Uranus", 2872.5, 51118, 30589, 27],
        ["Neptune", 4495.1, 49528, 59800, 14]]
    print("Welcome to Planetary Top Trumps!")
    print("You will get a random card.")
    print("You must choose the highest of four attributes against your opponents card.")
    print("If so you win!")
    reset()

def reset():
    global i, x
    lengthp = (len(Planets)-1)
    while True:
        i = random.randint(0, lengthp)
        x = random.randint(0, lengthp)
        if i != x:
            break
    title.delete(0, tk.END)
    title.insert(0, Planets[i][0])
    dfsent.delete(0, tk.END)
    dfsent.insert(0, Planets[i][1])
    sent.delete(0, tk.END)
    sent.insert(0, Planets[i][2])
    opent.delete(0, tk.END)
    opent.insert(0, Planets[i][3])
    noment.delete(0, tk.END)
    noment.insert(0, Planets[i][4])

def game(statchoice):
    if Planets[i][statchoice] > Planets[x][statchoice]:
        print("Opponent had:", Planets[x][0], "-->", Planets[x][statchoice])
        print("You Win!")
    elif Planets[i][statchoice] == Planets[x][statchoice]:
        print("Opponent had:", Planets[x][0], "-->", Planets[x][statchoice])
        print("Draw!")
    else:
        print("Opponent had:", Planets[x][0], "-->", Planets[x][statchoice])
        print("You Lose!")
    reset()


def dfsch():
    game(1)

def sch():
    game(2)

def opch():
    game(3)

def nomch():
    game(4)

import tkinter as tk
import random
GUI()
main()

