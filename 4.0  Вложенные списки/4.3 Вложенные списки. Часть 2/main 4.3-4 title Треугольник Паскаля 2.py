import math

def pascal(num):
	list_pascal = []
	for i in range(0,num):
		for m in range(0, i + 1):
			c = math.factorial(i) / (math.factorial(m) * math.factorial(i - m))
			list_pascal.append(int(c))
		print(*list_pascal)
		list_pascal = []

n = int(input())

pascal(n)
