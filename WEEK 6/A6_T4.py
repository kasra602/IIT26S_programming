print("Program starting.")
print("This program analyses a list of names from a file.")

filename = input("Insert filename to read: ")

print('Reading names from "{}".'.format(filename))

file = open(filename, "r", encoding="utf-8")

name_count = 0
total_length = 0
shortest_name = ""
longest_name = ""

print("Analysing names...")

while True:
    line = file.readline()

    if len(line) == 0:
        break

    line = line.strip()

    if len(line) == 0:
        continue

    name_count += 1

    if name_count == 1:
        shortest_name = line
        longest_name = line

    if len(line) < len(shortest_name):
        shortest_name = line

    if len(line) > len(longest_name):
        longest_name = line

    total_length += len(line)

file.close()

if name_count > 0:
    average_length = total_length / name_count
    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print("Name count -- {}".format(name_count))
    print("Shortest name -- {} chars".format(len(shortest_name)))
    print("Longest name -- {} chars".format(len(longest_name)))
    print("Average name -- {:.2f} chars".format(average_length))
    print("#### REPORT END ####")
else:
    print("No valid names found in the file.")

print("Program ending.")