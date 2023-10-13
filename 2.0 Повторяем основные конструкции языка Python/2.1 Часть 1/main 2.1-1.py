import math


def sum(a, b):
	sum = a + b
	return sum


def dif(a, b):
	dif = a - b
	return dif


def composit(a, b):
	composit = a * b
	return composit


def quot(a, b):
	quot = a / b
	return quot


def the_whole_part_of_division(a, b):
	TWPOD = a // b
	return TWPOD


def the_remainder_of_the_division(a, b):
	TROTD = a % b
	return TROTD


def the_root_of_ten(a, b):
	TROT = math.sqrt(math.pow(a, 10) + math.pow(b, 10))
	return TROT


a = int(input())
b = int(input())

print(sum(a, b))
print(dif(a, b))
print(composit(a, b))
print(quot(a, b))
print(the_whole_part_of_division(a, b))
print(the_remainder_of_the_division(a, b))
print(the_root_of_ten(a, b))
