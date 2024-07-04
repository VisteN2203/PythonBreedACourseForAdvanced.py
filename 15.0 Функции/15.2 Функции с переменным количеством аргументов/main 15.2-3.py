def mean(*args):
    number = 0.0
    count = 0
    for data in args:
        if type(data) is float or type(data) is int:
            number += float(data)
            count += 1
    if count == 0:
        return count
    else:
        return number / count

print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))



