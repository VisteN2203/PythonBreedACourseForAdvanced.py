n, list,list_two = int(input()),[],[]

[list.append(str(input()).split()) for k in range(n)]

for i in range(n):
	list[i].reverse()
	for j in range(n-i-1):
		del list[i][0]

for k in range(len(list)):
	for l in range(len(list[k])):
		list_two.append(int(list[k][l]))

print(max(list_two))