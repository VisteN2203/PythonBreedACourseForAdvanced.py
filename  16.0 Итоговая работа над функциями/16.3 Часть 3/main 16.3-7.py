def compose(a, b):
    return lambda x: a(b(x))