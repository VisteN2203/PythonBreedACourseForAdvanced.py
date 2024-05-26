n = int(input())

dict_synonyms = dict()

for _ in range(n):
	word = str(input()).split(" ")
	dict_synonyms[word[0]] = word[1]

synonym = str(input())

for key,value in dict_synonyms.items():
	if synonym == key:
		print(value)
	elif synonym == value:
		print(key)




