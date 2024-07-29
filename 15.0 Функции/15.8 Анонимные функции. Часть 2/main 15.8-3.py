is_non_negative_num = lambda x: set(x.replace('.', '', 1)) <= set('0123456789')

print(is_non_negative_num( '.0123456789'))




