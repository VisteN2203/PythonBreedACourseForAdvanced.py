list_num = [str(number) for number in str(input()).split()]

count = 0
string_two = ""
for i in range(1, len(list_num) // 2 + 1):
	string_two += " " + list_num[i + count] + " " + list_num[(i - 1) + count]
	count += 1

print(string_two.lstrip(), end="")
if len(list_num) % 2 != 0:
	print(" " + list_num[len(list_num) - 1])
