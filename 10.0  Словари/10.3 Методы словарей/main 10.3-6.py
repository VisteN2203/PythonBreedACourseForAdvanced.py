lst = [word.strip('.,!?:;-') for word in input().lower().split()]

dict_word = dict()
for word in lst:
	dict_word[word] = dict_word.get(word,0) + 1


list_min_word = []

for key, value in dict_word.items():
	if value == min(sorted(dict_word.values())):
		list_min_word.append(key)

print(min(list_min_word))
