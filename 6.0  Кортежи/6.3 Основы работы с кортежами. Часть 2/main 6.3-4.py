numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

list = [[] for _ in range(len(numbers))]

for i in range(len(numbers)):
	for j in range(len(numbers[i])):
		list[i].append(numbers[i][j])

list_two= []

for i in range(len(list)):
		list_two.append(sum(list[i]) / len(list[i]))

print(list_two)