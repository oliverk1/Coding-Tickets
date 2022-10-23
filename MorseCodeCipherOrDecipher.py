def Encryption(message):
    Cipher = []
    for i in message:
        if i != " ":
            Cipher.append(MorseCodeEncryption[i])
        elif i == " ":
            Cipher.append(" ")
    Cipher = " ".join(Cipher)
    return Cipher

def Decipher(message):
    Decipher = []
    for i in message:
        if i != " ":
            Decipher.append(MorseCodeDecipher[i])
        elif i == " ":
            Decipher.append(" ")
    Decipher = " ".join(Decipher)
    return Decipher

def ValidDecipher():
    while True:
        message = []
        while True:
            letter = input("Type in a letter. (If a space then leave blank and if finished type end.) ")
            if letter != "end" and letter != "":
                message.append(letter)
            elif letter !="end" and letter == "" or letter == " ":
                message.append(" ")
            else:
                break
            currentmessage=" ".join(message)
            print("Current Message:",currentmessage)
        try:
            for i in message:
                if i != " ":
                    MorseCodeDecipher[i]
        except KeyError:
            print("Invalid Character Detected.")
        else:
            break
    return message

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

def ValidChoice():
    while True:
        Choice = input("Would you like to encrypt (1) or decipher (2) a message in morse code? ")
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
        Rerun = input("Would you like to encrypt or decipher another message? Y/N ")
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
MorseCodeDecipher = {".-":"A", "-...":"B",
              "-.-.":"C", "-..":"D", ".":"E",
              "..-.":"F", "--.":"G", "....":"H",
              "..":"I", ".---":"J", "-.-":"K",
              ".-..":"L", "--":"M", "-.":"N",
              "---":"O", ".--.":"P", "--.-":"P",
              ".-.":"R", "...":"S", "-":"T",
              "..-":"U", "...-":"V", ".--":"W",
              "-..-":"X", "-.--":"Y", "--..":"Z",
              ".----":"1", "..---":"2", "...--":"3",
              "....-":"4", ".....":"5", "-....":"6",
              "--...":"7", "---..":"8", "----.":"9",
              "-----":"0", "--..--":", ", ".-.-.-":". ",
              "..--..":"? ", "-..-.":"/", "-....-":"-",
              "-.--.":"(", "-.--.-":")", " ":" "}
loop = True
while loop == True:
    choice=ValidChoice()
    if choice == 1:
        message = ValidMessage()
        print("The Cipher is:",Encryption(message))
    elif choice == 2:
        message = ValidDecipher()
        print("The Decipher is:",Decipher(message))
    loop = ValidRerun()
    if loop == False:
        end = input("")

