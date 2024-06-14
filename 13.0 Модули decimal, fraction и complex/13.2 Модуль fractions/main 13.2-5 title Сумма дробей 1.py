from fractions import Fraction

n = int(input())

drop = Fraction()

for i in range(1, n + 1):
	drop += Fraction(1,i ** 2)

print(drop)
