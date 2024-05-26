n = int(input())

dict_list = dict()
for i in range(n):
	text = str(input()).split(":")
	dict_list[text[0].lower()] = text[1].strip()

m = int(input())
list_keys = [str(input()).lower() for _ in range(m)]

for word in list_keys:
	if word in dict_list:
		print(dict_list[word])
	else:
		print("Не найдено")

