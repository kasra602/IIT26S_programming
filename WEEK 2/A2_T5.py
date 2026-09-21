#in the A2_T5 task it says first letter but in the example it shows the last letter. Use the last letter not the first letter.
print("Program starting.")
string1 = input("Insert a closed compund word: ")
string1length = len(string1)
string1lastletter = string1[-1]
string1slice1 = int(input("1) Starting point: "))
string1slice2 = int(input("2) Ending point: "))
string1slice3 = int(input("3) Step point: "))
string1substring1 = string1[string1slice1:string1slice2:string1slice3]
print("The word you inserted is '", string1,"' and in reverse it is '", string1[::-1],"'.", sep="")
print("The inserted word length is ", string1length)
print("Last character is ", string1lastletter)
print("Take substring from the insterted word by inserting...")
print("The word '", string1, "' sliced to the defined substring is '", string1substring1, "'.", sep="")
print("program ending.")