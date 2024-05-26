text = str(input())

dict_symbols = dict()
for symbol in text:
	dict_symbols[symbol] = dict_symbols.get(symbol,0) + 1

dict_letter = dict()
for i in range(int(input())):
	key, value = str(input()).split(": ")
	dict_letter[key] = int(value)

for letter in text:
	num = dict_symbols[letter]
	for key, value in dict_letter.items():
		if num == value:
			print(key,end="")