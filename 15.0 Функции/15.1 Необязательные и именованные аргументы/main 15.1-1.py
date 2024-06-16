# def matrix(num_one, num_two, num_three):
# 	list = [[num_three for i in range(num_two)] for _ in range(num_one)]
# 	return list
#
#
# num_one = input()
# num_two = input()
# num_three = input()
#
# if num_one == '':
# 	num_one = 1
#
# if num_two == '':
# 	num_two = num_one
#
# if num_three == '':
# 	num_three = 0
#
# print(matrix(int(num_one), int(num_two), int(num_three)))

def matrix(n=1, m=None, value=0):
	if m == None:
		m = n
	matrix = [[value] * m for _ in range(n)]
	return matrix

