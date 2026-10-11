print("Program starting.")
userinput = int(input("Insert a positive integer: "))
sequencetotal = 0
if userinput > 1:
    print(userinput, end=" -> ")
else:
    print(userinput, end=" ")
while userinput != 1:
    if userinput % 2 == 0:
        userinput = userinput // 2
    else:
        userinput = (userinput * 3) + 1
    sequencetotal += 1
    if userinput > 1:
        print(userinput, end=" -> ")
    else:
        print(userinput, end="")
print("\nSequence had", sequencetotal, "total steps.")
print("\nProgram ending.")