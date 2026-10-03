print ("Program starting.\n")
print("Options:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    Celsius = float(input("Insert the amount of Celsius: "))
    CtoF = Celsius * 9 / 5 +32
    print(Celsius,"°C equals to", CtoF,"°F")
    print("Program ending.")
elif choice == 2:
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    FtoC = (Fahrenheit - 32) / 1.8
    FtoC = round(FtoC, 1)
    print (Fahrenheit, "°F equals to", FtoC,"°C")
    print("Program ending.")
elif choice == 0:
    print("Exiting...")
    print("Program ending.")
else:
    print("Unknown option.")
    print("Program ending.")