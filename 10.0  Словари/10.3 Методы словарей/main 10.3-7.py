s = input().split()
my_dict = {}
my_list = []

for i in s:
	if i not in my_list:
		my_list.append(i)
	else:
		my_dict[i] = my_dict.get(i,0) + 1
		my_list.append(i + "_" + str(my_dict[i]))

print(*my_list)