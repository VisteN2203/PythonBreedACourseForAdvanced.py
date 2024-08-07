from functools import reduce

file = open("../Files/numbers.txt", "r", encoding="utf-8")

lines = file.readlines()

print(reduce(lambda x, y: int(x) + int(y), lines))

file.close()