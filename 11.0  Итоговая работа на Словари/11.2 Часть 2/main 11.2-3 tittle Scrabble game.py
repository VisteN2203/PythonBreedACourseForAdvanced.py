dict_letter= {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

count = 0
for letter in str(input()):
	for key, value in dict_letter.items():
		if letter.upper() in value:
			count += key

print(count)