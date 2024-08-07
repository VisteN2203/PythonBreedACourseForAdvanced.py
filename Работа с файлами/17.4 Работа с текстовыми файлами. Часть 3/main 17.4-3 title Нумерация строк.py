with open("../Files/input.txt", "r", encoding="utf-8") as read_file:
    with open("../Files/output.txt", "w", encoding="utf-8") as write_file:
        for number, string in enumerate(read_file.readlines(), 1):
            write_file.write(f"{number}) {string}")