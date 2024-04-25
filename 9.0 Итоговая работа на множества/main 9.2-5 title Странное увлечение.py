set_one_list = {int(i) for i in str(input()).split()}

set_two_list = {int(j) for j in str(input()).split()}

if set_one_list.isdisjoint(set_two_list) == True:
	print("BAD DAY")
else:
	print(*sorted(set_one_list & set_two_list, reverse=True, key=int))