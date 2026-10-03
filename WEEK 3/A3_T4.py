print ("Program starting")
print ("This is a program with simple menu, where you can choose which operation the program performs.")
username = str(input("Before the menu, please insert your name: "))
namelength = len(username)
print ("\nOptions: \n1 - Print welcome message\n2 - Print the name backwards\n3 - Print the first character\n4 - Show the amount of characters in the name\n0 - Exit")
answer = int(input("Your choice: "))
if answer == 1:
    print("Welcome ", username, "!", sep="")
    print ("Program ending.")
elif answer == 2:
    print("Your name backwards is", username[::-1])
    print ("Program ending.")
elif answer == 3:
    print("The first character of your name is '", username[0],"'", sep="")
    print ("Program ending.")
elif answer == 4:
    print("The amount of characters in your name is", namelength, "characters long.")
    print ("Program ending.")
elif answer == 0:
    print ("Program ending.")
else:
    print ("Unknown option.")
    print ("Program ending.")