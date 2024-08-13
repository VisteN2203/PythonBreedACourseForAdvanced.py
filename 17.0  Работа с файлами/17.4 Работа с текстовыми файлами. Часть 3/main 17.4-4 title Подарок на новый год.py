with open("../Files/class_scores.txt", "r", encoding="utf-8") as file_reade:
	with open("../Files/new_scores.txt", "w", encoding="utf-8") as file_write:
		for data in file_reade.readlines():
			name, number = data.split()
			file_write.write(f"{name} {int(number) + 5 if int(number) + 5 <= 100 else 100}\n")
