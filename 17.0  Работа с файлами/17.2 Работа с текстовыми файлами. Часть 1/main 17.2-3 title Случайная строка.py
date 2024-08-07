import random

file = open("../Files/lines.txt", "r", encoding="utf-8")

lines = file.readlines()

random_number = random.randint(0, len(lines))

print(lines[random_number])

file.close()