from fractions import Fraction

n = int(input())

set_numbers = set()
for i in range(1,n + 1):
	for j in range(1, n + 1):
		fuck = Fraction(i, j)
		if fuck.denominator > fuck.numerator:
			set_numbers.add(fuck)

for num in sorted(set_numbers):
	print(num)