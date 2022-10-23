def RemoveVowel(String):
    NewString = String
    for i in String:
        if i in Vowels:
            NewString = NewString.replace(i, "")
    return NewString

def CountVowel(String):
    Count=0
    for i in String:
        if i in Vowels:
            Count=Count+1
    return Count

def ValidChoice():
    while True:
        Choice = input("Would you like remove vowels from a string (1), count vowels in a string (2) or both (3)? ")
        try:
            Choice = int(Choice)
        except ValueError:
            print("Please enter either 1,2 or 3.")
            continue
        if 1 <= Choice <= 3:
            break
        else:
            print("Please enter either 1,2 or 3.")
    return Choice

def ValidRerun():
    while True:
        Rerun=input("Would you like to try another string? Y/N ")
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
    return Rerun

Vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
loop=True
while loop==True:
    String = input("Please input a string. ")
    Choice = ValidChoice()
    if Choice == 1:
        NewString = RemoveVowel(String)
        print("Without Vowels:", NewString)
    elif Choice == 2:
        Count = CountVowel(String)
        print("There are", Count, "vowels in", String)
    elif Choice == 3:
        NewString = RemoveVowel(String)
        Count = CountVowel(String)
        print("There are", Count, "vowels in", String)
        print("Without Vowels:", NewString)
    loop = ValidRerun()
    if loop == False:
        end = input("")

