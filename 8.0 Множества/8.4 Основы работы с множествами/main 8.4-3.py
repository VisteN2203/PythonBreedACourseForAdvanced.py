numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}

numbers_2 = set()

for i in numbers:
	numbers_2.add(i ** 2)

print(sum(numbers_2))


