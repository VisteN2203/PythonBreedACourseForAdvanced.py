from functools import reduce as r

eval = lambda coef, x: r(lambda v, c: c + v * x, map(int, coef))
print(eval(input().split(), int(input())))