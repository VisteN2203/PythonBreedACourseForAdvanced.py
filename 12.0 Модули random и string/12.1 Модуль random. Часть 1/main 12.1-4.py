import random

set_numbers = set()
while len(set_numbers) != 7:
	random_num = random.randint(1,49)
	set_numbers.add(random_num)

print(*sorted(set_numbers))


