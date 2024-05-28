import random

num = int(input())

list_friends = list(str(input()) for i in range(num))

dict_friends = dict()

while len(dict_friends) != len(list_friends):
	name_one, name_two = random.sample(list_friends, 2)
	dict_friends[name_one] = name_two


for key, value in dict_friends.items():
	print(key + " - " + value)

