numbers_one = set([int(i) for i in str(input()).split()])
numbers_two = set([int(j) for j in str(input()).split()])

set_numbers = numbers_one & numbers_two
sorted_set_numbers = sorted(set_numbers)
print(*sorted_set_numbers,end="")
