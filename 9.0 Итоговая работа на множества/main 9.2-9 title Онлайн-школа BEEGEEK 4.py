set_names_students_one = {i for i in str(input()).split()}

set_names_students_two = {i for i in str(input()).split()}

print(*sorted(set_names_students_one | set_names_students_two))