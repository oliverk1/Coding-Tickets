def button_clicked():
    messageent.delete(0, tk.END)
    if ValidCardNum() == True:
        messageent.insert(0, "Card Accepted.")
    else:
        messageent.insert(0, "Card Invalid.")
        
    
def reset():
    messageent.delete(0, tk.END)
    cardnum.delete(0, tk.END)
    expmon.delete(0, tk.END)
    expyr.delete(0, tk.END)
    security.delete(0, tk.END)

def ValidCardNum():
    cnum = cardnum.get()
    total = 0
    try:
        cardNumberint = int(cnum)
    except ValueError:
        return False
    if len(cnum) == 16:
        num = [int(i) for i in cnum]
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
            return False
        else:
            cnum = int(cnum)
            if ValidCardExp() == True:
                return True
    else:
        return False

def ValidCardExp():
    year = datetime.date.today().year
    month = datetime.date.today().month
    cardExpMonth = expmon.get()
    cardExpYear = expyr.get()
    try:
        cardExpYear = int(cardExpYear)
    except ValueError:
        y = False
    else:
        y = True
    try:
        cardExpMonth = int(cardExpMonth)
    except ValueError:
        m = False
    else:
        m = True
    if m == True and y == True:
        if cardExpYear > year and len(str(cardExpYear)) == 4 and cardExpMonth < 13 or cardExpYear == year and cardExpMonth >= month and len(str(cardExpYear)) == 4 and cardExpMonth < 13:
            cardExpYear = [str(i) for i in str(cardExpYear)]
            cardExpYear = cardExpYear[2:4]
            cardExpYear = int("".join(cardExpYear))
            if ValidThreeNum() == True:
                return True

def ValidThreeNum():
    ThreeNum = security.get()
    try:
        ThreeNum = int(ThreeNum)
    except ValueError:
        return False
    if len(str(ThreeNum)) > 3:
        return False
    else:
        return True

def main():
    global messageent, cardnum, expmon, expyr, security
    window = tk.Tk()
    window.geometry("450x315")
    window.config(bg="#f5f5f5")
    frame = tk.Label(bg="#f5f5f5")
    frame2 = tk.Label(bg="#f5f5f5")
    frame3 = tk.Label(bg="#f5f5f5")
    cardnumlbl = tk.Label(text = "Please enter your card number:", bg = "#f5f5f5")
    cardnum = tk.Entry()
    expmonlbl = tk.Label(text = "Expiry month (##):", bg = "#f5f5f5")
    expmon = tk.Entry()
    expyrlbl = tk.Label(text = "Expiry year (####):", bg = "#f5f5f5")
    expyr = tk.Entry()
    securitylbl = tk.Label(text = "Security code (###):", bg = "#f5f5f5")
    security = tk.Entry()
    button = tk.Button(text = "Done.", command = button_clicked, bg = "#f5f5f5")
    button2 = tk.Button(text = "Reset.", command = reset, bg = "#f5f5f5")
    messageent = tk.Entry()
    cardnumlbl.pack()
    cardnum.pack()
    expmonlbl.pack()
    expmon.pack()
    expyrlbl.pack()
    expyr.pack()
    securitylbl.pack()
    security.pack()
    frame.pack()
    button.pack()
    frame2.pack()
    button2.pack()
    frame3.pack()
    messageent.pack()


    
import datetime
import tkinter as tk
main()
