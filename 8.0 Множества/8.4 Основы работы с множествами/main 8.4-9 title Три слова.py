text = str(input())

set_one, set_two, set_three = set(), set(), set()
[set_one.add(i) for i in text.split()[0]]
[set_two.add(j) for j in text.split()[1]]
[set_three.add(k) for k in text.split()[2]]

if set_one == set_two == set_three:
	print("YES")
else:
	print("NO")







