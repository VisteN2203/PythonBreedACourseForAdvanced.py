num = int(input())

anton = ["a","n","t","o","n"]
word = ""
number_letter = 0
for i in range(num):
	text = str(input())
	for j in text:
		if j.lower() == anton[number_letter]:
			word += j.lower()
			number_letter += 1
			if number_letter == 5:
				break
	if word == "anton":
		print(i+1,end=" ")
		number_letter = 0
		word = ""
	else:
		number_letter = 0
		word = ""
