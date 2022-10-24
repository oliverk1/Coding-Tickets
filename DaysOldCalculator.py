def GetBirthday():
    while True:
        Birthday = ValidInt()
        bday = int(str(Birthday[:2]))
        bmonth = int(str(Birthday[2:4]))
        byear = int(str(Birthday[4:8]))
        if ValidDate(bday,bmonth,byear) == True and ValidTense(bday,bmonth,byear) == True:
            break
        else:
            print("Please try again with a correct date.")
    DaysOld(bday,bmonth,byear)

def DaysOld(bday,bmonth,byear):
    global day, month, year
    totaldays = (day-bday) + ((month-bmonth)*30.437) + ((year-byear)*365.24)
    totaldays = round(totaldays,2)
    print("You are",totaldays,"days old.")

def ValidInt():
    while True:
        Birthday = input("What is your birthday? ##/##/#### (Without the /) ")
        try:
            Birthdayint = int(Birthday)
        except ValueError:
            print("Please try again in correct format.")
            continue
        if len(Birthday) > 8:
            print("Please try again in correct format.")
        else:
            break
    return Birthday

def ValidDate(bday,bmonth,byear):
    leapyear = byear % 4
    if bday > 31:
        return False
    if bday == 31 and bmonth == 4 or bday == 31 and bmonth == 6 or bday == 31 and bmonth == 9 or bday == 31 and bmonth == 11:
        return False
    if bmonth == 2 and leapyear != 0 and bday > 28:
        return False
    if bmonth == 2 and leapyear == 0 and bday > 29:
        return False
    else:
        return True

def ValidTense(bday,bmonth,byear):
    global year, month, day
    if byear > year or byear == year and bmonth > month or byear == year and bmonth == month and bday > day:
        return False
    else:
        return True

def ValidRerun():
    while True:
        Rerun = input("Try another birthday? Y/N ")
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
        GetBirthday()
        if ValidRerun() == False:
            break
    end = input("")

import datetime
year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day
MainProgram()

