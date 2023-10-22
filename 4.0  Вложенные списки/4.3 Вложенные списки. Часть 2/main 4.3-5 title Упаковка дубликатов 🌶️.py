first_string = str(input()).replace(" ","")

list = [[first_string[0]]]

for i in range(1,len(first_string)):
	if first_string[i] != first_string[i-1]:
		list.append([first_string[i]])
	else:
		list[len(list)-1].append(first_string[i])

print(list)