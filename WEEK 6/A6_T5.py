SEPARATOR = ";"

def read_values(filename: str) -> str:
    """Reads numbers (one per row) and returns them separated with ;"""
    file = open(filename, "r", encoding="utf-8")
    values: str = ""
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        row = line.strip()
        if len(row) == 0:
            continue
        if len(values) > 0:
            values += SEPARATOR
        values += row
    file.close()
    return values


def analyse_numbers(values: str) -> str:
    """Analyses the numbers and returns the result as CSV text (header row + data row)."""
    if len(values) == 0:
        return "0;0;0;0"
    parts = values.split(SEPARATOR)
    count: int = 0
    total: int = 0
    greatest: int = int(parts[0])
    for part in parts:
        number = int(part)
        count += 1
        total += number
        if number > greatest:
            greatest = number
    average: float = total / count
    return str(count) + SEPARATOR + str(total) + SEPARATOR + str(greatest) + SEPARATOR + str(average)


def display_results(filename: str, results: str) -> None:
    parts = results.split(SEPARATOR)
    print("#### Number analysis - START ####")
    print('File "{0:s}" results:'.format(filename))
    print("Count;Sum;Greatest;Average")
    print("{0:s};{1:s};{2:s};{3:.2f}\n".format(parts[0], parts[1], parts[2], float(parts[3])))
    print("#### Number analysis - END ####")


def main() -> None:
    print("Program starting.")
    filename: str = input("Insert filename: ")
    values: str = read_values(filename)
    results: str = analyse_numbers(values)
    display_results(filename, results)
    print("Program ending.")


main()