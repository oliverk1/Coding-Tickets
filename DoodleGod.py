def MainProgram():
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
    #ONLY EPISODE 1 ELEMENTS
    print("Welcome to Doodle God!"
          "\nThe Goal is to Discover Every Element by Combining Other Elements."
          "\nIf at any point you want to exit type 'end'. Your Progress is tracked.")
    while True:
        elements = []
        with open("DoodleGod.txt", "r") as Input:
            lines = Input.readlines()
            for i in lines:
                as_list = i.split(",")
                elements.append(as_list[0].replace("\n",""))
        print("\033[1;37mThere are", 97 - len(elements), "elements left to discover.")
        print("Current Discovered Elements are:",', '.join(elements), "\n")
        element1 = input("Choose Element 1 to Combine: ")
        element2 = input("Choose Element 2 to Combine: ")
        if element1.lower() == "end" or element2.lower() == "end":
            break
        elif element1 in elements and element2 in elements:
            combinations = [element1 + element2, element2 + element1]
            for row in combinations:
                if row in recipes and recipes[row] not in elements:
                    print("\033[1;32mYou Discovered", recipes[row] + "!")
                    elements.append(recipes[row])
        elements.sort()
        with open("DoodleGod.txt", "w") as output:
            for row in elements:
                output.write(row + "\n")
        if len(elements) == 97:
            print("You Discovered Every Element!"
                  "\nWell Done!")
            break
    end = input("")

MainProgram()
