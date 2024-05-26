n_one = int(input())

list_dict = list()

for i in range(n_one):
	words = str(input()).split(" ")
	list_n = words[1:]
	list_dict.append({words[0] : list_n})

n_two = int(input())
list_city = list()
for j in range(n_two):
	list_city.append(str(input()))

for city in list_city:
	for dict_in_list in list_dict:
		for key, value in dict_in_list.items():
			if city in value:
				print(key)


