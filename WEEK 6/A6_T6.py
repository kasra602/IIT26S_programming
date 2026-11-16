LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def writeFile(Filename: str, Content: str):
    file = open(Filename, 'w', encoding="UTF-8")
    file.write(Content)
    file.close()

def askRows():
    print("Collecting plain text rows for ciphering.")
    Content: str = ""
    while True:
        Row = input("Insert row(empty stops): ")
        if len(Row) == 0:
            break
        Content += Row + "\n"
    return Content

def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13):
    Index = Alphabets.find(Character)
    return Alphabets[(Index + Shift) % len(Alphabets)]

def rot13(Content: str):
    Result: str = ""
    for Character in Content:
        if Character in LOWER_ALPHABETS:
            Result += shiftCharacter(Character, LOWER_ALPHABETS)
        elif Character in UPPER_ALPHABETS:
            Result += shiftCharacter(Character, UPPER_ALPHABETS)
        else:
            Result += Character
    return Result

def main():
    print("Program starting.")
    print()
    PlainText: str = askRows()
    CipheredText: str = rot13(PlainText)

    print()
    print("#### Ciphered text ####")
    print(CipheredText)
    print("#### Ciphered text ####")

    Filename: str = input("Insert filename to save: ")
    if len(Filename.strip()) == 0:
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        writeFile(Filename, CipheredText)
        print("Ciphered text saved!")
    print("Program ending.")

main()
