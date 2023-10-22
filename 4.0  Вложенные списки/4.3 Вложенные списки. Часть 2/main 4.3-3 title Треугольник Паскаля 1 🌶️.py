import math


def pascal(num):
	list_pascal = []
	for m in range(0, num + 1):
		c = math.factorial(num) / (math.factorial(m) * math.factorial(num - m))
		list_pascal.append(int(c))
	return list_pascal

n = int(input())

print(pascal(n))
