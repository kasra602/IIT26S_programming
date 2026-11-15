PROGRESS_FILE = "player_progress.txt"
HEADER = "current_location;next_location;passphrase"
SEPARATOR = ";"

LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13(text: str) -> str:
    result: str = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            index = LOWER_ALPHABETS.find(char)
            result += LOWER_ALPHABETS[(index + 13) % 26]
        elif char in UPPER_ALPHABETS:
            index = UPPER_ALPHABETS.find(char)
            result += UPPER_ALPHABETS[(index + 13) % 26]
        else:
            result += char
    return result


def get_location_name(location_id: int) -> str:
    if location_id == 0:
        return "home"
    elif location_id == 1:
        return "Galba's palace"
    elif location_id == 2:
        return "Otho's palace"
    elif location_id == 3:
        return "Vitellius' palace"
    else:
        return "Vespasian's palace"


def init_progress_file() -> None:
    """Creates the progress file if it does not exist yet."""
    try:
        file = open(PROGRESS_FILE, "r", encoding="utf-8")
        file.close()
    except FileNotFoundError:
        file = open(PROGRESS_FILE, "w", encoding="utf-8")
        file.write(HEADER + "\n")
        file.write("0;1;qvfpvcyvar\n")
        file.close()


def read_last_progress() -> str:
    """Returns the last data row of the progress file."""
    file = open(PROGRESS_FILE, "r", encoding="utf-8")
    last_row: str = ""
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        row = line.strip()
        if len(row) > 0 and row != HEADER:
            last_row = row
    file.close()
    return last_row


def read_message(filename: str) -> str:
    file = open(filename, "r", encoding="utf-8")
    message: str = ""
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        message += line
    file.close()
    return message


def find_message(next_id: int, cipher_pass: str, plain_pass: str) -> str:
    """Message file name uses the ciphered passphrase (plain as fallback)."""
    try:
        return read_message("{0:d}_{1:s}.gkg".format(next_id, cipher_pass))
    except FileNotFoundError:
        return read_message("{0:d}_{1:s}.gkg".format(next_id, plain_pass))


def append_progress(row: str) -> None:
    file = open(PROGRESS_FILE, "a", encoding="utf-8")
    file.write(row + "\n")
    file.close()


def save_plain_message(next_id: int, plain_pass: str, plain_message: str) -> None:
    file = open("{0:d}-{1:s}.txt".format(next_id, plain_pass), "w", encoding="utf-8")
    file.write(plain_message)
    file.close()


def main() -> None:
    init_progress_file()
    parts = read_last_progress().split(SEPARATOR)
    current_id = int(parts[0])
    next_id = int(parts[1])
    cipher_pass = parts[2]

    print("Travel starting.")
    if next_id > 4:
        print("All Emperors' messages have already been collected.")
        print("Travel ending.")
        return

    print("Currently at {0:s}.".format(get_location_name(current_id)))
    print("Travelling to {0:s}...".format(get_location_name(next_id)))
    print("...Arriving to the {0:s}.".format(get_location_name(next_id)))

    plain_pass = rot13(cipher_pass)
    print("Passing the guard at the entrance.")
    print('"{0:s}!"'.format(plain_pass.capitalize()))

    print("Looking for the message in the palace...")
    ciphered_message = find_message(next_id, cipher_pass, plain_pass)
    print("Ah, there it is! Seems cryptic.")

    # First line of the ciphered message -> progress file
    first_line = ciphered_message.split("\n")[0]
    append_progress("{0:d};{1:d};{2:s}".format(next_id, next_id + 1, first_line))
    print("[Game] Progress autosaved!")

    print("Deciphering Emperor's message...")
    save_plain_message(next_id, plain_pass, rot13(ciphered_message))
    print("Looks like I've got now the plain version copy of the Emperor's message.")

    print("Time to leave...")
    print("Travel ending.")


main()