count = 0

with open("../Files/grades.txt", "r", encoding="utf-8") as file:
	for line in file.readlines():
		list_num = [int(num) for num in line.split() if num.isdigit()]
		if all(map(lambda x: x >= 65, list_num)):
			count += 1
	print(count)


