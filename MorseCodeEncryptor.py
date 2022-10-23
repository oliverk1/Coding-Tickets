def Encryption(message):
    Cipher = []
    for i in message:
        if i != " ":
            Cipher.append(MorseCodeEncryption[i])
        elif i == " ":
            Cipher.append(" ")
    Cipher = " ".join(Cipher)
    return Cipher

def ValidMessage():
    while True:
        message = input("What message do you want encrypted? ")
        message = message.upper()
        try:
            for i in message:
                if i != " ":
                    MorseCodeEncryption[i]
        except KeyError:
            print("Invalid Character Detected.")
        else:
            break
    return message

def ValidRerun():
    while True:
        Rerun = input("Would you like to encrypt another message? Y/N ")
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

MorseCodeEncryption = { "A":".-", "B":"-...",
              "C":"-.-.", "D":"-..", "E":".",
              "F":"..-.", "G":"--.", "H":"....",
              "I":"..", "J":".---", "K":"-.-",
              "L":".-..", "M":"--", "N":"-.",
              "O":"---", "P":".--.", "Q":"--.-",
              "R":".-.", "S":"...", "T":"-",
              "U":"..-", "V":"...-", "W":".--",
              "X":"-..-", "Y":"-.--", "Z":"--..",
              "1":".----", "2":"..---", "3":"...--",
              "4":"....-", "5":".....", "6":"-....",
              "7":"--...", "8":"---..", "9":"----.",
              "0":"-----", ", ":"--..--", ".":".-.-.-",
              "?":"..--..", "/":"-..-.", "-":"-....-",
              "(":"-.--.", ")":"-.--.-", " ":" "}
loop = True
while loop == True:
    message = ValidMessage()
    print("The Cipher is:",Encryption(message))
    loop = ValidRerun()
    if loop == False:
        end = input("")

