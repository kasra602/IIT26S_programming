print ("Program starting.\nTesting decision structures.")
userinteger = int(input("Insert an integer: "))
userinput= int(input("Options: \n1 - In one multi branched decision\n2 - In multiple indenpendent if statements\n0 - Exit\nYour choice: "))

if userinput == 1:
    if userinteger >= 400:
        userinteger = userinteger + 44
        print("Using one multi branched decision structure.\n Result is", userinteger)
        print("\nProgram ending.")
    elif userinteger >= 200:
        userinteger = userinteger + 22
        print("Using one multi branched decision structure.\n Result is", userinteger)
        print("Program ending.")
    elif userinteger >= 100:
        userinteger = userinteger + 11
        print("Using one multi branched decision structure.\n Result is", userinteger)
        print("\nProgram ending.")
    else:
        print("Unkown option.\n\nProgram ending.")

elif userinput == 2:
    if userinteger >= 400:
        userinteger = userinteger + 44
        print("Using multiple indenpendent if statements structure.\nResult is ", userinteger)
        print("\nProgram ending.")
    if userinteger >= 200:
        userinteger = userinteger + 22
        print("Using multiple indenpendent if statements structure.\nResult is ", userinteger)
        print("\nProgram ending.")
    if userinteger >= 100:
        userinteger = userinteger + 11
        print("Using multiple indenpendent if statements structure.\nResult is ", userinteger)
        print("\nProgram ending.")

elif userinput == 0:
    print("Exiting...\n\nProgram ending.")

else:
    print("Unknown option.\n\nProgram ending.")