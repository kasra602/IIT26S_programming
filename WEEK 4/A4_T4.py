print("Program starting.")
wordcount = 0
howmanycharacters = 0
while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    wordcount += 1
    howmanycharacters += len(word)
print("\nYou inserted:\n", wordcount, "words\n", howmanycharacters, "characters")
print("\nProgram ending.")