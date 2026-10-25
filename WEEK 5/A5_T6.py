def Options():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def Choicee() -> int:
    Choice = input("Your choice: ")

    if Choice.isnumeric():
        return int(Choice)

    print("Unknown option!")
    return -1


def main():
    print("Program starting.")

    Count = 0

    while True:
        Options()
        Choice = Choicee()

        if Choice == 1:
            print(f"Current count - {Count}")
            print()

        elif Choice == 2:
            Count = Count + 1
            print("Count increased!")
            print()

        elif Choice == 3:
            Count = 0
            print("Cleared count!")
            print()

        elif Choice == 0:
            print("Exiting program.")
            break

        elif Choice != -1:
            print("Unknown option!")
            print()

    print()
    print("Program ending.")


main()