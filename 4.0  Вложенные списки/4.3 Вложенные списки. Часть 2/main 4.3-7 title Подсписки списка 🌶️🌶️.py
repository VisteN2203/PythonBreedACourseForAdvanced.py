def sublists_of_the_list(text, list_data):

	for i in range(len(text)):
		for j in range(len(text) - i):
			list_data.append(text[j:j + i + 1])

	return list_data


txt = str(input()).split()
list = [[]]

print(sublists_of_the_list(txt, list))
