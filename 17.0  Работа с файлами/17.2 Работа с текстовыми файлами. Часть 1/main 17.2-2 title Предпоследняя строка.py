file = open(str(input()), 'r', encoding='utf-8')

content = file.readlines()

print(content[-2])

file.close()