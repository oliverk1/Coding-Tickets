def FarenheitToCelsius(FarenheitNum):
    CelsiusNum = round(((FarenheitNum - 32) * (5 / 9)) , 2)
    return CelsiusNum

def CelsiusToFarenheit(CelsiusNum):
    FarenheitNum = round(((CelsiusNum * (9 / 5)) + 32) , 2)
    return FarenheitNum

def ValidChoice():
    while True:
        Choice = input("Would you like to convert degrees Farenheit to Celsius (1) or degrees Celsius to Farenheit (2)? ")
        try:
            Choice = int(Choice)
        except ValueError:
            print("Please enter either 1 or 2.")
            continue
        if 0 < Choice <= 2:
            break
        else:
            print("Please enter either 1 or 2.")
    return Choice

def ValidUserNum():
    while True:
        UserNum = input("What number is it you'd like to convert? ")
        try:
            UserNum = float(UserNum)
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            break
    return UserNum

def ValidRerun():
    while True:
        Rerun=input("Would you like to convert another number? Y/N ")
        try:
            Rerun = str(Rerun)
        except ValueError:
            print("Please enter Y/N.")
            continue
        if Rerun == "Y" or Rerun == "y":
            return True
            break
        elif Rerun == "N" or Rerun == "n":
            return False
            break
        else:
            print("Please enter Y/N.")
    return UserNum

loop=True
while loop==True:
    Choice = ValidChoice()
    UserNum = ValidUserNum()
    if Choice == 1:
        ConvertedNum = FarenheitToCelsius(UserNum)
        print(ConvertedNum, "degrees Celsius.")
    elif Choice == 2:
        ConvertedNum = CelsiusToFarenheit(UserNum)
        print(ConvertedNum, "degrees Farenheit.")
    loop=ValidRerun()
    if loop==False:
        end=input("")




