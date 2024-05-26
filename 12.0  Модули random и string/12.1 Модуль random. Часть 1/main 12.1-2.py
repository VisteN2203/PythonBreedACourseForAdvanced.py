import random

n = int(input())    # количество попыток

for _ in range(n):
	random_num = random.randint(1, 6)
	print(random_num)


