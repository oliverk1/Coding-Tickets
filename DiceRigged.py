import matplotlib.pyplot as plt
import numpy as np
import scipy

def getRolls():
    while True:
        rolls = input("How many dice rolls? ")
        try:
            rolls = int(rolls)
        except ValueError:
            print("Please try again in correct format.")
            continue
        else:
            break
    return rolls

def getSides():
    while True:
        sides = input("How many sides? ")
        try:
            sides = int(sides)
        except ValueError:
            print("Please try again in correct format.")
            continue
        else:
            break
    return sides

def ValidRerun():
    while True:
        Rerun = input("Would you like roll a die? Y/N ")
        if Rerun.upper() == "Y":
            return True
            break
        elif Rerun.upper() == "N":
            return False
            break
        else:
            print("Please enter Y/N.")
    return Rerun

def rollDie():
    open("DiceRigged.txt", "w").close()
    rolls = getRolls()
    for i in range(rolls):
        dice = input("")
        with open("DiceRigged.txt", "a") as f:
            f.write(dice+"\n")
            
def isRigged():            
    with open("DiceRigged.txt", "r") as f:
        for row in f:
            outcome = row.replace("\n","")
            diceOutcome.append(int(outcome))
    sides = getSides()
    freq = max(set(diceOutcome), key=diceOutcome.count)
    count = diceOutcome.count(freq)
    probability = round(((count/len(diceOutcome))*100),2)
    for i in range(sides):
        totalCount.append(diceOutcome.count(i+1))   
    pvalue = ((scipy.stats.chisquare(totalCount))[1])
    if pvalue <= 0.05:
        print("Dice is rigged:"
              "\nChance to roll",freq,"is",str(probability)+"%"
              "\nShould be:",str(round(((1/sides)*100),1))+"%",
              "\nP-Value:",round(pvalue,2))
    else:
        print("Dice is not rigged:"
              "\nP-Value:",round(pvalue,2))
    plt.figure("Dice Probability")
    plt.hist(diceOutcome, bins = sides)
    plt.xlabel("Dice Outcome")
    plt.ylabel("Count")
    plt.title("Dice Probability")
    plt.show()

diceOutcome = []
totalCount = []
if ValidRerun() is True:
    rollDie()
isRigged()
