import math


def IMT(weight, height):
	IMT = weight / (math.pow(height, 2))

	if 18.5 <= IMT <= 25:
		return "Оптимальная масса"
	elif IMT < 18.5:
		return "Недостаточная масса"
	else:
		return "Избыточная масса"


weight = float(input())
height = float(input())

print(IMT(weight, height))
