with open("../Files/file.txt","r") as file:
	reading_file = file.read()
	print("Input file contains:")
	print(f"{len([i for i in reading_file if i.isalpha()])} letters")
	print(f"{len(reading_file.split())} words")
	file.seek(0)
	print(f"{len(file.readlines())} lines")

str = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated."

print(len(str))