result = {}
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

set_letter = set(text)


for letter in set_letter:
	for letter_text in text:
		if letter_text == letter:
			result[letter] = result.get(letter, 0) + 1





