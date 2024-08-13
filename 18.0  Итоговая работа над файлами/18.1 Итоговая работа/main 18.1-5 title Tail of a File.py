with open("../Files/test_file.txt","r",encoding="utf-8") as file:
	text = file.read().split("\n")
	print(*text[-10:],sep="\n")