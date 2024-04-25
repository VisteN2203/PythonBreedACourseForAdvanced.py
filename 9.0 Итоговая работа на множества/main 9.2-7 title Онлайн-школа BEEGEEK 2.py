m,n = int(input()), int(input())

set_students_math = {str(input()) for i in range(m)}

set_students_informatics = {str(input()) for j in range(n)}

print(len(set_students_math - set_students_informatics))

