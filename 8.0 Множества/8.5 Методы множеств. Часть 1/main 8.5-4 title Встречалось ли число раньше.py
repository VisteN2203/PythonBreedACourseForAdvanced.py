numbers = input().split()

set_numbers = set()
for i in numbers:
	if i.lstrip("0") not in set_numbers:
		print("NO")
		set_numbers.add(i)
	else:
		print("YES")