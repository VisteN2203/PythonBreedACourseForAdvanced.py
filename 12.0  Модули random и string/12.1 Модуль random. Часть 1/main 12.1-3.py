import random

length = int(input())    # длина пароля

for _ in range(length):
	random_num = random.randint(0,1)
	if random_num == 1:
		random_letter = random.randint(65,90)
		print(chr(random_letter), end="")
	elif random_num == 0:
		random_letter = random.randint(97,122)
		print(chr(random_letter),end="")


