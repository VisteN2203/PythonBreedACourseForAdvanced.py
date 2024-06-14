import random

num = int(input())

list_friends = list(str(input()) for i in range(num))

dict_friends = dict()

while len(list_friends) != len(dict_friends):
	for name in list_friends:
		random_name = random.choice(list_friends)
		if random_name not in dict_friends.values() and random_name != name:
			dict_friends[name] = random_name


for key, value in dict_friends.items():
	print(key + " - " + value)

