numbers_words = int(input())

set_word = set()
for i in range(numbers_words):
	word = input().lower()
	for j in word:
		set_word.add(j)
	print(len(set_word))
	set_word.clear()