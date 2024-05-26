word_one = str(input()).lower()
word_two = str(input()).lower()

dict_word_one = dict()
dict_word_two = dict()

for i in word_one:
	if i not in ".,!?:;-" and i != " ":
		dict_word_one[i] = dict_word_one.get(i, 0) + 1

for j in word_two:
	if j not in ".,!?:;-" and j != " ":
		dict_word_two[j] = dict_word_two.get(j, 0) + 1

if dict_word_one == dict_word_two:
	print("YES")
else:
	print("NO")


