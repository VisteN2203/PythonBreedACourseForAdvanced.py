name_and_text = str(input())

with open(name_and_text,"r",encoding="utf-8") as file:
	print(len(file.readlines()))
