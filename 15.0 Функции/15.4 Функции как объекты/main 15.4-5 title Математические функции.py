import math

def square_function(num):
	return pow(num, 2)

def cube_function(num):
	return pow(num, 3)

def root_function(num):
	return math.sqrt(num)

def module_function(num):
	return math.fabs(num)

def sinusoidal_function(num):
	return math.sin(num)

n = int(input())
text = str(input())

dict_functional = {"квадрат" : square_function, "куб" : cube_function, "корень" : root_function,
				   "модуль" : module_function, "синус" : sinusoidal_function}

print(dict_functional[text](n))