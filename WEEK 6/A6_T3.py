def copytext(Filename: str):
     filehandler = open(Filename, 'r')
     content = ''
     Row = filehandler.readline()
     while Row != '':
         content += Row
         Row = filehandler.readline()
     filehandler.close()
     return content
def getfileinputs():
    filename = input("Insert source filename: ")
    filename2 =  input("Insert destination filename: ")
    return filename, filename2
def main():
    print("program starting.")
    filename, filename2 = getfileinputs()
    print("Reading file", filename,"content.\nFile content ready in memory.")
    content = copytext(filename)
    print("Writing content into file", filename2)
    filehandler = open(filename2, 'w')
    filehandler.write(content)
    filehandler.close()
    print("copying operation complete.")
    print("program ending.")
    return None
main()