def DecimalToBinary(num):
    global binarynum
    if num >= 1:
        DecimalToBinary(num // 2)
    add = num % 2
    binarynum.append(add)
    return binarynum

def ListToString(binarylist,num):
    if num != 0:
        binarylist.remove(0)
    binaryappend = "".join([str(i) for i in binarylist])
    return binaryappend

def BinaryToDecimal(num):
    length = len(num)+1
    multiplier = 1
    decimal = 0
    for i in range(1,length):
        current = num[-i] * multiplier
        decimal = decimal + current
        multiplier = multiplier * 2
    return decimal

def ValidBinary():
    while True:
        while True:
            num = input("Enter the binary number. ")
            try:
                Binary = [int(x) for x in str(num)]
            except ValueError:
                print("Please only input 1 or 0's.")
            else:
                break
        Binary = [int(x) for x in str(num)]
        length = len(Binary)
        invalid = False
        for i in range(length):
            if Binary[i] != 1 and Binary[i] != 0:
                invalid = True
        if invalid == False:
            break
        else:
            print("Please only input 1 or 0's.")
    return Binary

def ValidUserNum():
    while True:
        UserNum = input("What number is it you'd like to convert to binary? ")
        try:
            UserNum = int(UserNum)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if UserNum < 0:
            print("Please enter a positive number.")
        else:
            break
    return UserNum

def ValidChoice():
    while True:
        Choice = input("Would you like to convert from decimal to binary (1) or binary to decimal (2)? ")
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

def ValidRerun():
    while True:
        Rerun = input("Would you like to convert another number? Y/N ")
        if Rerun == "Y" or Rerun == "y":
            return True
            break
        elif Rerun == "N" or Rerun == "n":
            return False
            break
        else:
            print("Please enter Y/N.")

def MainProgram():
    global binarynum
    while True:
        binarynum = []
        Choice = ValidChoice()
        if Choice == 1:
            UserNum = ValidUserNum()
            binarylist = DecimalToBinary(UserNum)
            print("Binary:", ListToString(binarylist, UserNum))
        elif Choice == 2:
            Binary = ValidBinary()
            print("Decimal:", BinaryToDecimal(Binary))
        if ValidRerun() == False:
            break
    end = input("")

binarynum=[]
MainProgram()




