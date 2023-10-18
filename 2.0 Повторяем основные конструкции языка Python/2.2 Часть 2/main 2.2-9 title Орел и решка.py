list_text = [letter for letter in str(input())]

count,max_count = 0, 0
for i in range(len(list_text)):
	if list_text[i] == "Р":
		count += 1
		max_count = max(max_count, count)
	else:
		count = 0

print(max_count)