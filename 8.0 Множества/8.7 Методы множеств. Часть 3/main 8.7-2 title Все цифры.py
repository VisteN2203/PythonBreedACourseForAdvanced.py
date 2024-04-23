num_one, num_two = set(input()), set(input())

if num_two.issubset(num_one):
	print("YES")
else:
	print("NO")