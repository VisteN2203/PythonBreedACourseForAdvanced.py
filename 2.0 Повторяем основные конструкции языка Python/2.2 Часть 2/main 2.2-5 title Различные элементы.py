list_num = input().split()
list_count = []

for i in range(len(list_num)):
	if list_num[i] not in list_count:
		list_count.append(list_num[i])

print(len(list_count))