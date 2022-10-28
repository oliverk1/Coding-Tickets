def main():
    global Planets, OpponentCards
    while True:
        Planets = [["Mercury", 57.9, 4879, 88, 0],
           ["Venus", 108.2, 12104, 224.7, 0],
           ["Earth", 149.6, 12756, 365.2, 1],
           ["Mars", 227.9, 6792, 687, 2],
           ["Jupiter", 778.6, 142984, 4331, 67],
           ["Saturn", 1433.5, 120536, 10747, 64],
           ["Uranus", 2872.5, 51118, 30589, 27],
           ["Neptune", 4495.1, 49528, 59800, 14]]
        print("Welcome to Planetary Top Trumps!")
        time.sleep(0.3)
        print("You will start with four planet cards.")
        time.sleep(0.3)
        print("You must choose the highest of four attributes against your opponents card.")
        time.sleep(0.3)
        print("If so you win their card. You win when you have all their cards.")
        time.sleep(0.3)
        OpponentCards = []
        for i in range(4):
            length = len(Planets)-1
            randnum = random.randint(0, length)
            OpponentCards.append(Planets[randnum])
            Planets.remove(Planets[randnum])
        count = 0
        opcount = 0
        while True:
            if len(Planets) > 0 and len(OpponentCards) > 0:
                print("\nYou have",len(Planets),"cards.")
                time.sleep(0.3)
                game(count, opcount)
                if (count + 1) >= len(Planets):
                    count = 0
                else:
                    count = count + 1
                if (opcount + 1) >= len(OpponentCards):
                    opcount = 0
                else:
                    opcount = opcount + 1
            elif len(Planets) > 0 and len(OpponentCards) == 0:
                print("\nWell done! You Won!")
                break
            else:
                print("\nYou Lost!")
                break
        if ValidRerun() == False:
            break
    end = input("")

def game(i, x):
    print("Planet:", Planets[i][0])
    time.sleep(0.3)
    print("Distance from Sun (10^6km):", Planets[i][1])
    time.sleep(0.3)
    print("Size (Diameter in km):", Planets[i][2])
    time.sleep(0.3)
    print("Orbital Period:", Planets[i][3])
    time.sleep(0.3)
    print("Number of Moons:", Planets[i][4])
    time.sleep(0.3)
    while True:
        statchoice = input("Which stat will you choose? (1-4) ")
        time.sleep(0.3)
        try:
            statchoice = int(statchoice)
        except ValueError:
            print("ERROR")
            time.sleep(0.3)
            continue
        if 1 <= statchoice <= 4:
            break
        else:
            print("ERROR")
            time.sleep(0.3)
    if Planets[i][statchoice] > OpponentCards[x][statchoice]:
        print("Opponent had:", OpponentCards[x][0], "-->", OpponentCards[x][statchoice])
        time.sleep(0.3)
        print("You Win!")
        Planets.append(OpponentCards[x])
        OpponentCards.remove(OpponentCards[x])
    elif Planets[i][statchoice] == OpponentCards[x][statchoice]:
        print("Opponent had:", OpponentCards[x][0], "-->", OpponentCards[x][statchoice])
        time.sleep(0.3)
        print("Draw!")
    else:
        print("Opponent had:", OpponentCards[x][0], "-->", OpponentCards[x][statchoice])
        time.sleep(0.3)
        print("You Lose!")
        OpponentCards.append(Planets[i])
        Planets.remove(Planets[i])
    time.sleep(0.3)

def ValidRerun():
    while True:
        Rerun = input("Would you like to play again? Y/N ")
        time.sleep(0.3)
        if Rerun == "Y" or Rerun == "y":
            return True
            break
        elif Rerun == "N" or Rerun == "n":
            return False
            break
        else:
            print("Please enter Y/N.")
            time.sleep(0.3)

import random
import time
main()
