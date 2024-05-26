dict_numbers = dict()

for i in range(int(input())):
	value, key = str(input()).lower().split(" ")
	dict_numbers[key] = dict_numbers.get(key, []) + [value]

for j in range(int(input())):
	name = str(input()).lower()
	print(*dict_numbers.get(name, ["абонент не найден"]))






