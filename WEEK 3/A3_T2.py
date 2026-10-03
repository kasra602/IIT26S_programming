print ("Program starting.")
print ("String comparisons")
word = input("Insert first word: ")
character = input("Insert a character: ")
if character in word:
    print("Word '", word, "' contains character '", character,"'", sep="")
word2 = input("Insert second word: ")
if word > word2:
    print("The second word '", word2,"' is before the first word '", word,"' alphabetically.", sep="")
elif word < word2:
    print("The second word '", word2,"' is after the first word '", word,"' alphabetically.", sep="")
print ("Program ending.")