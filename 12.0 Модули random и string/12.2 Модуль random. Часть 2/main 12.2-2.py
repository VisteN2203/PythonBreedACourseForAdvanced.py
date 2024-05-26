import random

list_letter = list(range(65,91))
list_num = list(range(0,99))
def generate_index():
    string = chr(random.choice(list_letter)) + chr(random.choice(list_letter)) + str(random.choice(list_num))
    return string + "_" + string[::-1]


print(generate_index())

