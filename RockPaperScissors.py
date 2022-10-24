def RockPaperScissors(choice):
    RPS = ["rock", "paper", "scissors"]
    Random = random.randint(0,2)
    ToBeat = RPS[Random]
    if choice == ToBeat:
        print("Tie")
        win = 2
    elif choice == "rock" and ToBeat == "scissors" or choice == "paper" and ToBeat == "rock" or choice == "scissors" and ToBeat == "paper":
        print("You win!")
        win = 1
    else:
        print("You lose!")
        win = 0
    WinCount(win)

def WinCount(win):
    global count
    global totalwin
    if win != 2:
        totalwin = totalwin + win
        count = count + 1
        winpercentageunrounded = (totalwin/count)*100
        winpercentage = round(winpercentageunrounded, 2)
        print("You have won",winpercentage,"% of games.")

def ValidChoice():
    while True:
        choice = input("Rock, Paper, Scissors? ")
        choice = choice.lower()
        if choice == "rock" or choice == "paper" or choice == "scissors":
            break
        else:
            print("Please enter a valid choice.")
    return choice

def ValidRerun():
    while True:
        Rerun = input("Play Again? Y/N ")
        if Rerun == "Y" or Rerun == "y":
            return True
            break
        elif Rerun == "N" or Rerun == "n":
            return False
            break
        else:
            print("Please enter Y/N.")

def MainProgram():
    while True:
        choice = ValidChoice()
        RockPaperScissors(choice)
        if ValidRerun() == False:
            break
    end=input("")

import random
totalwin = 0
count = 0
MainProgram()


