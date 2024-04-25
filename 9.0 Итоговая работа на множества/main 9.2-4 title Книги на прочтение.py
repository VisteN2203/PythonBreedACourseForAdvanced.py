m,n = int(input()), int(input())

set_books_in_home = [str(input()) for i in range(m)]

set_books_for_summer = [str(input()) for j in range(n)]

for i in set_books_for_summer:
	if i in set_books_in_home:
		print("YES")
	else:
		print("NO")
