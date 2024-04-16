n = int(input())

list_people = [input().split() for _ in range(n)]

good_list = [list_people[i] for i in range(n) if "5" in list_people[i] or "4" in list_people[i]]
correct_list = list_people + [[]] + good_list
for k in range(len(correct_list)):
	print(*correct_list[k])

