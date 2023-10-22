n = int(input())
list = []

for i in range(1,n + 1):
	for j in range(1, i + 1):
		list.append(j)
	print(list)
	list = []