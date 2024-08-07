def pretty_print(data, side='-', delimiter='|'):
	strings = ""
	for elem in data:
		strings += f'{delimiter} {elem} '

	print(" " + (len(strings + delimiter) - 2) * side)
	print(strings + delimiter)
	print(" " + (len(strings + delimiter) - 2) * side)

pretty_print([1, 2, 10, 23, 123, 3000])


