with open(str(input()),encoding="utf-8") as word_file:
	with open("../Files/forbidden_words.txt",encoding="utf-8") as forbidden_file:
		forbidden_file = forbidden_file.read().split()
		for s in word_file:
			for x in forbidden_file:
				while x in s.lower():
					index = s.lower().index(x)
					s = s[:index] + "*" * len(x) + s[index+len(x):]
			print(s.strip())

