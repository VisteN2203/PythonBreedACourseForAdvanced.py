n = int(input())
matrix = []
list = [[],[],[],[]]

[matrix.append(str(input()).split()) for k in range(n)]

for i in range(n):
	for j in range(n):
		if i < j and i < n - 1 - j:
			list[0].append(int(matrix[i][j]))
		elif i < j and i > n - 1 - j:
			list[1].append(int(matrix[i][j]))
		elif i > j and i > n - 1 - j:
			list[2].append(int(matrix[i][j]))
		elif i > j and i < n - 1 - j:
			list[3].append(int(matrix[i][j]))

print(f"Верхняя четверть: {sum(list[0])}")
print(f"Правая четверть: {sum(list[1])}")
print(f"Нижняя четверть: {sum(list[2])}")
print(f"Левая четверть: {sum(list[3])}")