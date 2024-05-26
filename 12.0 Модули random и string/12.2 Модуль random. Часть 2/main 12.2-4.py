import random

set_numbers = set()

while len(set_numbers) != 100:
    random_num = random.randint(1000000,9999999)
    set_numbers.add(random_num)

for num in set_numbers:
    print(num)