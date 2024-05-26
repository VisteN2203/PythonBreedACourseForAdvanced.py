figures = {"0": "zero",
		   "1": "one",
		   "2": "two",
		   "3": "three",
		   "4": "four",
		   "5": "five",
		   "6": "six",
		   "7": "seven",
		   "8": "eight",
		   "9": "nine"}

number = [i for i in str(input())]

list_figures = list()
for j in number:
	list_figures.append(figures[j])

print(*list_figures)
