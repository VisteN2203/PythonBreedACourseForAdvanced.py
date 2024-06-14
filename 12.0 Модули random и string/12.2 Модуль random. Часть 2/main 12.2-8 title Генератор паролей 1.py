import random
from string import *


def generate_password(length):
	LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
	password = ""
	for num in range(length):
		password += random.choice(LETTER)

	return password
n, m = int(input()), int(input())

for i in range(n):
	print(generate_password(m))
