import requests

def getChoice():
    while True:
        choice = input("Would you like to:"
                   "\n1) Search for a Cocktail"
                   "\n2) List all Cocktails by First Letter"
                   "\n3) Lookup a Random Cocktail"
                       "\n")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid. Please try again.")
            continue
        if 0 < int(choice) < 4:
            break
        else:
            continue
    return choice

def listByLetter():
    while True:
        letter = input("What letter do you want to search?"
                       "\n")
        num = letter.isnumeric()
        if 0 < len(letter) < 2 and num == False:
            break
        else:
            print("Please type a letter.")
            continue
    letterList = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=" + str(letter))
    letterList = letterList.json()
    letterDrink = letterList["drinks"]
    for row in letterDrink:
        print(row["strDrink"])

def randomCocktail():
    cocktailList = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    cocktailList = cocktailList.json()
    return cocktailList

def getCocktail():
    while True:
        cocktailChoice = input("What is the name of the cocktail?"
                           "\n")
        cocktailChoice = cocktailChoice.replace(" ", "+")
        cocktailList = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + str(cocktailChoice))
        cocktailList = cocktailList.json()
        if str(cocktailList["drinks"]) != "None":
            break
        else:
            print("Cocktail Not Found. Please try again.")
            continue
    return cocktailList

def getAlcoholic(drink):
    if str(drink["strAlcoholic"]) == "Alcoholic":
        alcoholic = "Yes"
    else:
        alcoholic = "No"
    return alcoholic

def getIngredients(drink):
    ingredients = []
    for i in range(15):
        ingTitle = "strIngredient"+str(i+1)
        meaTitle = "strMeasure"+str(i+1)
        if str(drink[ingTitle]) != "None":
            ingredients.append([drink[meaTitle],drink[ingTitle]])
    return ingredients

def cocktailDetails(cocktailList):
    drink = cocktailList["drinks"]
    drink = drink[0]
    alcoholic = getAlcoholic(drink)
    ingredients = getIngredients(drink)
    instructions = drink["strInstructions"]
    instructions = instructions.replace(". ","\n-")
    print("Cocktail:", str(drink["strDrink"]),
          "\nAlcoholic:", alcoholic,
          "\nCocktail glass:", str(drink["strGlass"]),
          "\nIngredients:")
    for row in ingredients:
        if str(row[0]) != "None":
            print("-"+str(row[0]),str(row[1]))
        else:
            print("-"+str(row[1]))
    print("Instructions:\n-"+str(instructions))

def main():
    choice = getChoice()
    if choice == 1:
        cocktailDetails(getCocktail())
    elif choice == 2:
        listByLetter()
    elif choice == 3:
        cocktailDetails(randomCocktail())

main()
end = input("")