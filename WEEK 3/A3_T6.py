choice = int(input("Program starting.\nOptions:\n1. Length\n2. Weight\n3. Exit\nYour choice: "))
if choice == 1:
    choice2 = int(input("1. Meters to kilometers\n2. Kilometers to meters\n3. Exit\nYour choice: "))
    if choice2 == 1:
        meters = float(input("Insert meters: "))
        m2k = meters / 1000
        m2k = round(m2k, 1)
        print(meters,"m is",m2k,"km\nProgram ending.")
    elif choice2 == 2:
        kilometers = float(input("Insert kilometers: "))
        k2m = kilometers * 1000
        k2m = round(k2m, 1)
        print(kilometers,"km is",k2m,"m\nProgram ending.")
    elif choice2 == 0:
        print("Exiting...\nProgram ending.")
    else:
        print("Unknown option.\nProgram ending.")
elif choice == 2:
    choice2 = int(input("1. Grams to pounds\n2. Pounds to grams\n3. Exit\nYour choice: "))
    if choice2 == 1:
        Grams = float(input("Insert grams: "))
        g2p = (Grams / 453.59237)
        g2p = round(g2p, 1)
        print(Grams,"g is",g2p,"lb\nProgram ending.")
    elif choice2 == 2:
        Pounds = float(input("Insert pounds: "))
        p2g = Pounds * 453.59237
        p2g = round(p2g, 1)
        print(Pounds,"lb is",p2g,"g\nProgram ending.")
    elif choice2 == 0:
        print("Exiting...\nProgram ending.")
    else:
        print("Unknown option.\nProgram ending.")
elif choice == 0:
    print("Exiting...\nProgram ending.")
else:
    print("Unknown option.\nProgram ending.")