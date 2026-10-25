def askname():
    name = input("Insert name: ")
    return name
def greetuser(name):
    print("Hello ", name,"!", sep="")
def main():
    print("Program starting.")
    name = askname()
    greetuser(name)
    print("Program ending.")
main()