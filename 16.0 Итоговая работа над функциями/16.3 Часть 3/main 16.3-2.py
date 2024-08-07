from functools import reduce
def product_of_odds_new(data):
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)






def product_of_odds_old(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result

print(product_of_odds_new([1,2,3,4,5,6,7,8,9]))