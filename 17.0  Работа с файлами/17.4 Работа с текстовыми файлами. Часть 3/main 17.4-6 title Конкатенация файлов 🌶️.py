with open("../Files/output.exe","w",encoding="utf-8") as file_writing:
	for _ in range(int(input())):
		with open(str(input()), "r", encoding="utf-8") as file_reading:
			file_writing.write(file_reading.read())
