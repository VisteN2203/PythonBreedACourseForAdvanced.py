from fractions import Fraction

n = int(input())

set_numbers = set()
for i in range(1,n + 1):
	for j in range(2,n):
		fuck = Fraction(i,j)
		if fuck.denominator > fuck.numerator and fuck.denominator + fuck.numerator == n:
			set_numbers.add(fuck)

print(max(set_numbers))