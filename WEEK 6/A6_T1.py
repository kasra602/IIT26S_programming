def readFile(Filename: str):
    filehandler = open(Filename, 'r')
    content = ''
    Row = filehandler.readline()
    while Row != '':
        content += Row
        Row = filehandler.readline()
    filehandler.close()
    return content

def main():
    print("program starting.")
    print("this program can read a file.")
    Filename = input("Insert filename: ")
    filecontent = readFile(Filename)
    print("#### START", Filename, "####")
    print(filecontent)
    print("#### END", Filename, "####")
    print("program ending.")
    return None
main()