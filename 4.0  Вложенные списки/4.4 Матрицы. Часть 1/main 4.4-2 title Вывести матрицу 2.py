n, m = int(input()), int(input())

list = []
for i in range(n):
	list.append([])
	for j in range(m):
		list[i].append(str(input()))
		print(list[i][j],end=" ")
	print()

print()

for k in range(m):
	for l in range(n):
		print(list[k][l],end="")
	print()