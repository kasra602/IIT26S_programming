def getvariables():
    name = input("Enter your name: ")
    lastname = input("Enter your last name: ")
    filename = input("Enter filename: ")
    return name, lastname, filename
def savevariables(name, lastname, filename):
    filehandler = open(filename, 'w')
    filehandler.write(name + '\n')
    filehandler.write(lastname + '\n')
    filehandler.close()
    return None
def main():
    print("program starting.")
    name, lastname, filename = getvariables()
    savevariables(name, lastname, filename)
    print("program ending.")
    return None
main()