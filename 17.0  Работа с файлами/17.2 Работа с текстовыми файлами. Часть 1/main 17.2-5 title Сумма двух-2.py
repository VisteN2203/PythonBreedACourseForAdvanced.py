from functools import reduce

file = open("../Files/nums.txt", "r", encoding="utf-8")

lines = file.read().split()

print(reduce(lambda x,y : int(x) + int(y), lines))

file.close()