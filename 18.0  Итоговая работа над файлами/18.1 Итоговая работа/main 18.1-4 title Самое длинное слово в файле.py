with open("../Files/words.txt","r",encoding="utf-8") as file:
	text = file.read().split()
	max_len_in_text = max([len(i) for i in text])
	print(*filter(lambda x: len(x) == max_len_in_text, text),sep="\n")

