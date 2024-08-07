from functools import reduce

file = open("../Files/prices.txt", "r", encoding="utf-8")

data = [i[:len(i)-2:].split("\t") for i in file.readlines()]
numbers = [int(j[1]) * int(j[2])  for j in data]

print(reduce(lambda x,y: x + y, numbers) * 10)

file.close()