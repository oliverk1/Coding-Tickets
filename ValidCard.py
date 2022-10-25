#Using length and the Luhn algorithm to validate card number,
#length and todays date to verify expiration date
#and length to verify security code.
def ValidCardNum():
    while True:
        total = 0
        cardNumber = input("Please enter card number: ")
        try:
            cardNumberint = int(cardNumber)
        except ValueError:
            print("Invalid card number.")
            continue
        if len(cardNumber) == 16:
            num = [int(i) for i in cardNumber]
            for i in range(1,17):
                digit = num[i-1]
                if (i % 2) != 0:
                    digit = num[i-1]
                    digit = digit * 2
                    if digit > 9:
                        digit = str(digit)
                        digit = [int(i) for i in digit]
                        digit = digit[0] + digit[1]
                total = total + digit
            if (total % 10) != 0:
                print("Invalid card number.")
            else:
                cardNumber = int(cardNumber)
                ThreeNum, CardExpMonth, CardExpYear = ValidCardExp()
                Card = [cardNumber, CardExpMonth, CardExpYear, ThreeNum]
                print("Valid card entered. Thank you.")
                return Card
                break
        else:
            print("Invalid card number.")

def ValidCardExp():
    year = datetime.date.today().year
    month = datetime.date.today().month
    while True:
        cardExpYear = input("Please enter expiry year. ")
        try:
            cardExpYear = int(cardExpYear)
        except ValueError:
            print("Invalid expiry year.")
            continue
        cardExpMonth = input("Please enter expiry month. ")
        try:
            cardExpMonth = int(cardExpMonth)
        except ValueError:
            print("Invalid expiry month.")
            continue
        if cardExpYear > year and len(str(cardExpYear)) == 4 and cardExpMonth < 13 or cardExpYear == year and cardExpMonth >= month and len(str(cardExpYear)) == 4 and cardExpMonth < 13:
            cardExpYear = [str(i) for i in str(cardExpYear)]
            cardExpYear = cardExpYear[2:4]
            cardExpYear = int("".join(cardExpYear))
            ThreeNum = ValidThreeNum()
            return ThreeNum, cardExpMonth, cardExpYear
            break
        else:
            print("Invalid expiration date.")

def ValidThreeNum():
    while True:
        ThreeNum = input("Please enter security code. ")
        try:
            ThreeNum = int(ThreeNum)
        except ValueError:
            print("Invalid security code.")
            continue
        if len(str(ThreeNum)) > 3:
            print("Invalid Security Code.")
        else:
            return ThreeNum

import datetime
Card = ValidCardNum()


