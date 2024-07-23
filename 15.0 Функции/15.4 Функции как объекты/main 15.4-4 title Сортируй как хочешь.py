athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

def sorted_name(x):
	return x[0]

def sorted_age(x):
	return x[1]

def sorted_height(x):
	return x[2]

def sorted_weight(x):
	return x[3]

dict_athletes = {1 : sorted_name, 2 : sorted_age, 3 : sorted_height, 4 : sorted_weight}

command = int(input())

q = sorted(athletes, key=dict_athletes[command])

for i in q:
	print(*i)


