import random

with open("../Files/first_names.txt", "r") as first_file:
	with open("../Files/last_names.txt", "r") as second_file:
		first_line = first_file.read().split()
		second_line = second_file.read().split()
		zipline = list(zip(first_line, second_line))
		for i in range(3):
			print(*zipline[random.randint(0, len(zipline) - 1)])