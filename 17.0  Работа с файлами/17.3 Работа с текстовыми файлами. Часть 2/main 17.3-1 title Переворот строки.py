with open("../Files/text.txt","r", encoding="utf-8") as file:
	text = file.read()
	print(text[::-1])