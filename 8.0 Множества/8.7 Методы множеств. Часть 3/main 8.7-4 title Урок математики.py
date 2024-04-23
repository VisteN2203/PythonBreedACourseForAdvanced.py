num_one, num_two, num_three = set(str(input()).split()), set(str(input()).split()), set(str(input()).split())

set_student = (num_one | num_two | num_three) - ( num_one & num_two & num_three)

print(*sorted(set_student, key=int))