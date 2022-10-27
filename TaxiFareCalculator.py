def distance():
    while True:
        distance = input("How far are you travelling (km)? ")
        try:
            distance=float(distance)
        except ValueError:
            print("Try entering only numbers.")
            continue
        else:
            fare(distance)
            break

def fare(distance):
    fare = 2.8 + (1.5 * distance)
    fare = round(fare, 2)
    print("The fare is:",fare,"pounds.")

distance()
