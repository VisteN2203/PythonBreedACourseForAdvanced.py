import random

result_list = []
numbers_list = [i for i in range(1,76)]

for k in range(5):
    random_list = random.sample(numbers_list, 5)
    result_list.append(random_list)
    for num in random_list:
        numbers_list.remove(num)

result_list[2][2] = 0
for list in result_list:
    for number in list:
        print(str(number).ljust(3), end="")
    print()
