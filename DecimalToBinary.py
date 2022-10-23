def DecimalToBinary(num):
        if num >= 1:
            DecimalToBinary(num//2)
        add = num % 2
        binarynum.append(add)
        return binarynum

def ListToString(binarylist,num):
    if num != 0:
        binarylist.remove(0)
    binaryappend = "".join([str(i) for i in binarylist])
    return binaryappend

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
    return Rerun

loop=True
while loop==True:
    binarynum=[]
    UserNum = ValidUserNum()
    binarylist=DecimalToBinary(UserNum)
    print("Binary:", ListToString(binarylist,UserNum))
    loop=ValidRerun()
    if loop==False:
        end=input("")

