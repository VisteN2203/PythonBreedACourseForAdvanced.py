word_one = str(input())
word_two = str(input())

dict_word_one = dict()
dict_word_two = dict()

for i in word_one:
	dict_word_one[i] = dict_word_one.get(i, 0) + 1

for j in word_two:
	dict_word_two[j] = dict_word_two.get(j, 0) + 1

if dict_word_one == dict_word_two:
	print("YES")
else:
	print("NO")


