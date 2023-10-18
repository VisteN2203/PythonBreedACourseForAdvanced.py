list_num = [int(number) for number in input().split()]

total = 0

for i in range(1,len(list_num)):
	if list_num[i-1] < list_num[i]:
		total += 1

print(total)