numbers = [int(i) for i in str(input()).split()]

def plus(n):
	number = 0
	for i in str(n):
		number += int(i)
	return number

print(*sorted(numbers, key=plus))