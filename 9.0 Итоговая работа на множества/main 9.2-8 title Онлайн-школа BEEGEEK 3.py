m,n = int(input()), int(input())

set_students_math = {str(input()) for i in range(m)}

set_students_informatics = {str(input()) for j in range(n)}

if len(set_students_math ^ set_students_informatics) != 0:
	print(len(set_students_math ^ set_students_informatics))
else:
	print("NO")


