num_one, num_two, num_three = set(str(input()).split()), set(str(input()).split()), set(str(input()).split())

set_student = num_three - (num_one | num_two)

print(*sorted(set_student, reverse= True, key=int))