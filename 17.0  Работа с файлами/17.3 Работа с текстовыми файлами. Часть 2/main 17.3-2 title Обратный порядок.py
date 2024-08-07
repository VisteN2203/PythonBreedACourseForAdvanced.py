with open("../Files/data.txt", "r", encoding="utf-8") as file:
	data = file.readlines()
	for line in range(len(data) - 1, -1, -1):
		print(data[line][:-1:])
