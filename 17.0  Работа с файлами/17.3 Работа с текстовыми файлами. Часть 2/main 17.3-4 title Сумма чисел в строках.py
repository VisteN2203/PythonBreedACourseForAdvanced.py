with open("../Files/numbers (1).txt","r", encoding="utf-8") as file:
	numbers = [str(num).split() for num in file.read().split("\n")]
	numbers = [[int(i) for i in nums] for nums in numbers]
	result = list(map(sum, numbers))
	print(*result[:-1:], sep="\n")
