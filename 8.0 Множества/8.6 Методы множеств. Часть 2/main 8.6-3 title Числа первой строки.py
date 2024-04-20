numbers_one = set([int(i) for i in str(input()).split()])
numbers_two = set([int(j) for j in str(input()).split()])


print(*sorted(numbers_one - numbers_two))