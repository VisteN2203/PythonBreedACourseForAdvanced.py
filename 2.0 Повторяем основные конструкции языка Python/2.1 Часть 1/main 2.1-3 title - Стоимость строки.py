def from_a_letter_to_a_ruble(text):
	count_letters = len(text)
	sum_kopecks = 60 * count_letters
	kopecks = str(sum_kopecks)[2:]
	ruble = str(sum_kopecks)[:2]


	if sum_kopecks < 100:
		return f"0 р. {sum_kopecks} коп."
	else:
		if kopecks == "00":
			return f"{ruble} р. {kopecks[1:]} коп."
		else:
			return f"{ruble} р. {kopecks} коп."


txt = str(input())

print(from_a_letter_to_a_ruble(txt))