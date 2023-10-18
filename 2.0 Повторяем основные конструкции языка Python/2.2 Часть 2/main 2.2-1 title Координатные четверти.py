num = int(input())

one, two, three, four = 0, 0, 0, 0

for i in range(num):
	list_x_y = str(input()).split()
	x, y = int(list_x_y[0]), int(list_x_y[1])

	if x > 0 and y > 0:
		one += 1
	elif x < 0 and y > 0:
		two += 1
	elif x < 0 and y < 0:
		three += 1
	elif x > 0 and y < 0:
		four += 1

print(f"Первая четверть: {one}")
print(f"Вторая четверть: {two}")
print(f"Третья четверть: {three}")
print(f"Четвертая четверть: {four}")