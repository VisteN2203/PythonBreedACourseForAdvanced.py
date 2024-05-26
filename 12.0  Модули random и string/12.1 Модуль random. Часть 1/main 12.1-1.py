import random

n = int(input())    # количество попыток

for _ in range(n):
	random_num = random.randint(0, 1)
	if random_num == 1:
		print("Орел")
	else:
		print("Решка")



