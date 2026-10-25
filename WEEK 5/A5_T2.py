def framework(PWord):
    print("*" * (len(PWord) + 4))
    print("*",PWord, "*")
    print("*" * (len(PWord) + 4))
def main():
    print("Program starting.")
    word = input("Insert word: ")
    framework(word)
    print("Program ending.")
main()