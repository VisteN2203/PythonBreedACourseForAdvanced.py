n,m = int(input()),int(input())

list = [[int(i) for i in input().split()] for _ in range(n)]

list_index = [int(i) for i in input().split()]
for k in range(n):
	first_num = list[k][list_index[0]]
	second_num = list[k][list_index[1]]
	list[k][list_index[0]] = second_num
	list[k][list_index[1]] = first_num

for l in range(n):
	print(*list[l])