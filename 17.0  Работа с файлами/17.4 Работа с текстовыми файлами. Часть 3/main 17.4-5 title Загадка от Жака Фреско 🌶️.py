dict_colour_goat = dict()

with open("../Files/goats.txt", "r", encoding="utf-8") as read_file:
	with open("../Files/answer.txt", "w", encoding="utf-8") as write_file:
		for data in read_file.readlines():
			text = data.split()
			if text[0] != "COLOURS" and text[0] != "GOATS":
				dict_colour_goat[text[0]] = dict_colour_goat.get(text[0], -1) + 1

		for key, values in dict_colour_goat.items():
			if (sum(dict_colour_goat.values()) / 100) * values > 7:
				write_file.write(f"{key} goat\n")
