n, list, sum = int(input()), [], 0
[list.append(str(input()).split()) for k in range(n)]

for i in range(n):
	sum += int(list[i][i].strip())
print(sum)