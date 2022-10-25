def randomStreet():
    win = 0
    count = 0
    print("Welcome to the Monopoly Quiz! You have ten streets and you have to name their colour.")
    time.sleep(0.2)
    print("If it's a station put black. Good luck!")
    time.sleep(0.2)
    file = open("Monopoly.txt", "r")
    lines = file.readlines()
    file.close
    for i in range(10):
        randomLine = random.choice(lines)
        data = randomLine.split(";")
        streetName = data[0]
        colour = data[1].lower()
        lines.remove(randomLine)
        userGuess=input("What colour is " + streetName + "? ").lower()
        time.sleep(0.2)
        if userGuess != colour:
            count = count + 1
            print("Incorrect. It is",colour)
        else:
            count = count + 1
            win = win + 1
            print("Correct.")
        time.sleep(0.2)
    print("You won",win,"out of",count,"games.")
    if (win / count) > 0.5:
        print("Well done!")
    else:
        print("Better luck next time!")
    time.sleep(0.2)

def ValidRerun():
    while True:
        Rerun = input("Would you like to play Again? Y/N ")
        if Rerun == "Y" or Rerun == "y":
            return True
            break
        elif Rerun == "N" or Rerun == "n":
            return False
            break
        else:
            print("Please enter Y/N.")

def main():
    while True:
        randomStreet()
        if ValidRerun() == False:
            break
    end = input("")

import time
import random
main()

