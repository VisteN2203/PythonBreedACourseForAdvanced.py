num_one, num_two, num_three = set(str(input()).split()), set(str(input()).split()), set(str(input()).split())

set_student = set(k for k in range(11))
set_all_estimation = num_one | num_two | num_three
for i in set_all_estimation:
	if int(i) in set_student:
		set_student.discard(int(i))

print(*sorted(set_student, key=int))
