count_num, flag = int(input()), False
list_num, composition = [int(input()) for i in range(0, count_num)], int(input())

for i in range(0, len(list_num)):
	for j in range(0,len(list_num)):
		if list_num[i] * list_num[j] == composition and i != j:
			flag = True
			break

if flag == True:
	print("ДА")
else:
	print("НЕТ")