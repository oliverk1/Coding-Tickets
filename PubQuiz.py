def quiz():
    win = 0
    count = 0
    print("Welcome to the Pub Quiz!")
    time.sleep(0.2)
    file = open("PubQuiz.txt", "r")
    lines = file.readlines()
    file.close
    for i in range(10):
        randomLine = random.choice(lines)
        data = randomLine.split(";")
        question = data[0]
        answer = data[1].lower()
        lines.remove(randomLine)
        userGuess=input(question + " ").lower()
        time.sleep(0.2)
        if userGuess != answer:
            count = count + 1
            print("Incorrect. It is",answer)
        else:
            count = count + 1
            win = win + 1
            print("Correct.")
        time.sleep(0.2)
    print("You got",win,"out of",count,"questions right.")
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
        quiz()
        if ValidRerun() == False:
            break
    end = input("")

import random
import time
main()

