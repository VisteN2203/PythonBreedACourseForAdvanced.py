x, y = input()
y1 = ord(x) - 97
x1 = 8 - int(y)

matrix = [[str(".") for q in range(8)] for _ in range(8)]

for x2 in range(8):
	for y2 in range(8):
		if y1 == y2 and (x1 != x2):
			matrix[x2][y2] = "*"
		if x1 == x2 and (y1 != y2):
			matrix[x2][y2] = "*"
		if abs(x2-x1) == abs(y2-y1):
			matrix[x2][y2] = "*"

matrix[x1][y1] = "Q"

for k in range(8):
	print(*matrix[k])