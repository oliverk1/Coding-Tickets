def RockPaperScissors(choice):
    RPS = ["rock", "paper", "scissors"]
    Random = random.randint(0,2)
    ToBeat = RPS[Random]
    if choice == ToBeat:
        print("Tie")
    elif choice == "rock" and ToBeat == "scissors" or choice == "paper" and ToBeat == "rock" or choice == "scissors" and ToBeat == "paper":
        print("You win!")
    else:
        print("You lose!")

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
MainProgram()


