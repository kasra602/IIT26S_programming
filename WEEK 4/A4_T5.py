print("Program starting.\n")
startingpoint = int(input("Insert starting point: "))
stoppingpoint = int(input("Insert stopping point: "))
inspectionpoint = int(input("Insert inspection point: "))
if inspectionpoint < startingpoint or inspectionpoint > stoppingpoint:
    if startingpoint >= stoppingpoint:
        print("\nStarting point value must be less than the stopping point value.")
        print("Inspection value must be within the range of start and stop.")
        print("\nProgram ending.")
    else:
       print("\nInspection value must be within the range of start and stop.")
       print("\nProgram ending.")
     
else:
    print("\nFirst loop - insepction with break:")
    for i in range(startingpoint, stoppingpoint+1):
        if i == inspectionpoint:
            break
        print(i, end=" ")
    print("\nSecond loop - insepction with continue:")
    for i in range(startingpoint, stoppingpoint):
        if i == inspectionpoint:
            continue
        print(i, end=" ")
    print("\n\nProgram ending.")