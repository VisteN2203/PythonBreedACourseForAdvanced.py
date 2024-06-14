from decimal import *

num = Decimal(input())

formula = num.exp() + num.ln() + num.log10() + num.sqrt()

print(formula)