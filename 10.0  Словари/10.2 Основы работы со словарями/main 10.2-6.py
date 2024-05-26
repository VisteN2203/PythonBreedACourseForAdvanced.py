dictionary = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
	}

text = [i for i in str(input()).upper()]

text_numbers = ""

for letter in text:
	for keys, values in dictionary.items():
		if letter in values:
			text_numbers += (str(keys) * (values.index(letter) + 1))

print(text_numbers)



