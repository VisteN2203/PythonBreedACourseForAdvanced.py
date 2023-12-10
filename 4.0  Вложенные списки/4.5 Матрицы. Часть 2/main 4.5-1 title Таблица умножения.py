def multiplication_table():
	for i in range(n):
		for j in range(m):
			print(i * j,end=" ")
		print()

n,m = int(input()),int(input())

multiplication_table()