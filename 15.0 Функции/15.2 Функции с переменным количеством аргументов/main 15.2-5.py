def print_products(*args):
    count = 0
    for data in args:
        if type(data) is str and data != "":
            count += 1
            print(f"{count}) {data}")
    if count == 0:
        print("Нет продуктов")

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)