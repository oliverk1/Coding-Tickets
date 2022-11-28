def recipes():
    global recipes
    recipes = {"FireEarth": "Lava", "AirEarth": "Dust", "AirFire": "Energy",
               "AirEnergy": "Storm", "FireDust": "Ash", "LavaAir": "Stone",
               "FireStone": "Metal", "WaterStone": "Sand", "EnergyMetal": "Electricity",
               "WaterAir": "Steam", "MetalSteam": "Boiler", "FireSand": "Glass",
               "WaterEarth": "Swamp", "SwampSand": "Clay", "SwampEnergy": "Life",
               "SwampLife": "Bacteria", "WaterLife": "Weeds", "SwampWeeds": "Moss",
               "EarthMoss": "Grass", "SwampGrass": "Reed", "WaterBacteria": "Plankton",
               "LifeSand": "Seeds", "LifeAsh": "Ghost", "LifeStone": "Egg", "EggEarth": "Dinosaur",
               "DinosaurFire": "Dragon", "AirEgg": "Bird", "SwampMoss": "Fern", "ClayLife": "Golem",
               "GolemLife": "Human", "HumanFire": "Corpse", "LifeCorpse": "Zombie", "ZombieCorpse": "Ghoul",
               "HumanEnergy": "Wizard", "WizardEnergy": "Demigod", "SeedsEarth": "Tree", "HumanMetal": "Tools",
               "MetalTools": "Weapon", "WeaponHuman": "Hunter", "HunterWeapon": "Warrior",
               "WarriorDragon": "Hero", "DragonWarrior": "Blood", "BloodHuman": "Vampire",
               "FireClay": "Bricks", "ToolsReed": "Paper", "BirdHunter": "Meat", "HunterBird": "Feather",
               "TreeTools": "Wood", "FeatherPaper": "Book", "SwampBacteria": "Worm", "BacteriaSwamp": "Sulfur",
               "TreeFire": "Ash", "FireTree": "Coal", "CoalBoiler": "Steam-Engine", "SandWorm": "Snake",
               "SnakeWater": "Fish", "WaterCoal": "Oil", "PlanktonFish": "Whale", "SnakeTools": "Poison",
               "PoisonWeapon": "Poisoned Weapon", "Poisoned WeaponHuman": "Assassin", "WoodTools": "Wheel",
               "EarthTools": "Field", "FieldSeeds": "Wheat", "WheatStone": "Flour", "FlourWater": "Dough",
               "DoughFire": "Bread", "SandEgg": "Turtle", "SwampEgg": "Lizard", "WoodWheel": "Cart",
               "CartSteam-Engine": "Locomotive", "BirdFire": "Phoenix", "LizardEarth": "Beast",
               "BeastVampire": "Werewolf", "WormEarth": "Beetle", "BeetleSand": "Scorpion", "WoodWater": "Boat",
               "CartBeast": "Chariot", "HunterBeast": "Meat", "BeastHunter": "Wool", "HumanClay": "Ceramics",
               "HumanStone": "Hut", "StonePlankton": "Shells", "ShellsStone": "Limestone", "LimestoneClay": "Cement",
               "ToolsWool": "Fabric", "HumanBeast": "Domestic Animal", "Domestic AnimalGrass": "Milk",
               "GrassDomestic Animal": "Fertilizer", "LifeTree": "Treant", "WeedsEarth": "Mushroom",
               "WaterCement": "Concrete", "ConcreteBricks": "House", "FishBeast": "Dolphin",
               "WoodBoat": "Ship", "OilCart": "Car", "CarAir": "Airplane", "FabricHuman": "Clothes"}

def layout():
    global window, elements
    elements = []
    with open("DoodleGod.txt", "r") as Input:
        lines = Input.readlines()
        for i in lines:
            as_list = i.split(",")
            elements.append(as_list[0].replace("\n", ""))
    column2 = []
    for row in elements:
        column2.append([sg.Button(row, key=row)])
    column1 = [
        [sg.Text("Elements Left: " + str((97 - len(elements))), key = "COUNTER")],
        [sg.Text("", key="OPT1")],
        [sg.Text("", key="OPT2")],
        [sg.Text("", key="DISCOVERY", visible = False), sg.Button("OK", key = "OK", visible = False)],
        [sg.Button("Quit"), sg.Button("Refresh", key="REFRESH")]
    ]
    layout = [
        [sg.Column(column1),
         sg.VSeperator(),
         sg.Column(column2, key="ELEMENTS", scrollable = True, vertical_scroll_only = True), ]
    ]
    window = sg.Window("Doodle God", layout)

def updateelements(count, event):
    global element1, element2, run
    if (count % 2) == 0:
        element1 = event
        element2 = ""
        window["OPT1"].update(event)
        window["OPT2"].update("")
    else:
        window["OPT2"].update(event)
        element2 = event
    if element1 in elements and element2 in elements:
        combinations = [element1 + element2, element2 + element1]
        for row in combinations:
            if row in recipes and recipes[row] not in elements:
                window["DISCOVERY"].update("You Discovered " + recipes[row], visible = True)
                window["OK"].update(visible = True)
                elements.append(recipes[row])
                window.extend_layout(window["ELEMENTS"], [[sg.Button(recipes[row], key=recipes[row])]])
    elements.sort()
    with open("DoodleGod.txt", "w") as output:
        for row in elements:
            output.write(row + "\n")

def windowloop():
    count= 0
    while True:
        event, values = window.read()
        window["COUNTER"].update("Elements Left: " + str((96 - len(elements))))
        if event == "Quit" or event == sg.WIN_CLOSED:
            break
        elif event == "REFRESH":
            count = -1
            window.close()
            layout()
        elif event == "OK":
            window["OK"].update(visible=False)
            window["DISCOVERY"].update(visible=False)
            count -= 1
        else:
            updateelements(count, event)
        if len(elements) == 97:
            print("You Discovered Every Element!"
                  "\nWell Done!")
            break
        count += 1

def Main():
    sg.theme("Dark")
    recipes()
    layout()
    windowloop()
    window.close()

import PySimpleGUI as sg
Main()
