num_one, num_two = int(input()), int(input())

set_set = set()
[set_set.add(i) for i in str(num_one)]
[set_set.add(j) for j in str(num_two)]

if len(set_set) == 10:
	print("YES")
else:
	print("NO")


