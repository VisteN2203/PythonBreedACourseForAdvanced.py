from decimal import *
num = Decimal(input())

max = max(num.as_tuple().digits)
if int(num) == 0 :
	min = 0
else:
	min = min(num.as_tuple().digits)

print(min + max)
