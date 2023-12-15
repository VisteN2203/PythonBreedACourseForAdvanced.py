list = input().split()
num = int(input())
nums = 0
matrix = [[] for _ in range(num)]
for i in range((len(list) // num) + 1):
	for j in range(num):
		if nums + 1 <= len(list) - 1:
			nums = j + i * num
			matrix[j].append(list[nums])
		else:
			break

print(matrix)