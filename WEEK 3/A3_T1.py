print ("Program starting.")
print ("Insert two integers.")
num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))
print ("Comparing inserted integers.")
if num1 > num2:
    print ("First integer is greater.")
elif num1 < num2:
    print ("Second integer is greater.")
elif num1 == num2:
    print ("integers are the same.")
print ("\nAdding integers together.")
sum = num1 + num2
print (num1, "+", num2, "=", sum)
print ("\nChecking the parity of the sum...")
if sum % 2 == 0:
    print ("sum is even.")
else:
    print ("sum is odd.")
print ("Program ending.")