print ("Program starting.")
print ("This is a program with simple menu, where you can choose which operation the program performs.")
username = str(input("Before the menu, please insert your name: "))
print("\nOptions: \n 1 - Print welcome message\n 0 - Exit")
answer = int(input("Your choice: "))
if answer == 1:
    print("Welcome ", username, "!", sep="")
    print("Program ending.")
else:
    print("Program ending.")