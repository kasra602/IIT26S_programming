DELIMITER = ","
def collectWords() -> str:
    Words = ""

    while True:
        Word = input("Insert word(empty stops): ")

        if Word == "":
            break

        if Words == "":
            Words = Word
        else:
            Words = Words + DELIMITER + Word


    return Words


def analyseWords(PWords: str):
    if PWords == "":
        WordCount = 0
        CharacterCount = 0
        Average = 0.0
    else:
        WordList = PWords.split(DELIMITER)

        WordCount = len(WordList)
        CharacterCount = 0

        for Word in WordList:
            CharacterCount = CharacterCount + len(Word)

        Average = CharacterCount / WordCount

    print(f"- {WordCount} Words")
    print(f"- {CharacterCount} Characters")
    print("- {:.2f} Average word length".format(Average))


def main():
    print("Program starting.")

    Words = collectWords()
    analyseWords(Words)

    print("Program ending.")


main()