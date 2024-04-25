num = int(input())

set_city = {str(input()) for i in range(num)}

if str(input()) not in set_city:
	print("OK")
else:
	print("REPEAT")