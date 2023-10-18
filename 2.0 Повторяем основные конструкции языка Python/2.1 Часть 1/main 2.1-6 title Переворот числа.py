num = str(input())

if len(num) <= 5:
	num = num[::-1]
	while num.startswith("0"):
		num = num[1:]
	else:
		print(num)
else:
	new_num = num[-(len(num)):-5] + num[-1:-6:-1]
	while new_num.startswith("0"):
		new_num = new_num[1:]
	else:
		print(new_num)