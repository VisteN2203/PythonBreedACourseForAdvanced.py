m,n = int(input()), int(input())

list_students = [str(input()) for i in range(n + m)]

set_students_one = set()

set_students_two = set()

for j in list_students:
	if j not in set_students_one:
		set_students_one.add(j)
	else:
		set_students_two.add(j)



# set_students_one = {str(input()) for i in range(m)}
#
# set_students_two = {str(input()) for j in range(n)}

print(len(set_students_one ^ set_students_two) if len(set_students_one ^ set_students_two) > 0 else "NO")

