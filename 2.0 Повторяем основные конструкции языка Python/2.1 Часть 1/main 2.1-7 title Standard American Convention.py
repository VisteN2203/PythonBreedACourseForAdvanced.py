number = str(input())

total = 0
new_number = ""
for i in range(-1, -len(number) - 1, -1):
	if total == 3:
		new_number += ","
		new_number += str(number[i])
		total = 1
	else:
		total += 1
		new_number += str(number[i])

print(new_number[::-1])
