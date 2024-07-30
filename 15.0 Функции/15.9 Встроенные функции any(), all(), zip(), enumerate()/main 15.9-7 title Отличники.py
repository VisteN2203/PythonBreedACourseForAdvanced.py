list_in_list = [[str(input()) for j in range(int(input()))] for i in range(int(input()))]
result = []

for list in list_in_list:
	result.append(any(map(lambda x: x.split()[1] == "5", list)))

print("YES" if all(result) else "NO")