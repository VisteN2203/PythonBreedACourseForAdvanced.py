x, y = input()
x1 = ord(x) - 97
y1 = 8 - int(y)

matrix = [[str(".") for q in range(8)] for _ in range(8)]
matrix[y1][x1] = "N"



for x2 in range(8):
	for y2 in range(8):
		if abs(x2 - y1) * abs(y2 - x1) == 2:
			matrix[x2][y2] = "*"

for k in range(8):
	print(*matrix[k])
print()