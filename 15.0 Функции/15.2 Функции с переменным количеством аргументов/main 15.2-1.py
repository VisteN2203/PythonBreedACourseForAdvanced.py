def count_args(*args):
    return len(args)


print(count_args([], (''), 'a', 12, False))