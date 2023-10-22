def chunked(text, numbers):
	list = []
	len_text = len(text)
	a = len_text // numbers
	b = len_text % numbers
	if numbers <= len_text:
		for _ in range(0, a + b):
			list.append([])
	else:
		for _ in range(1):
			list.append([])

	for i in range(0, len(list) - b):
		for j in range(0,numbers):
			list[i].append(text[j])
		text = text[numbers:]

	for k in range(0, b):
		list[len(list) - 1].append(text[k])

	return list

txt = str(input()).replace(" ", "")
num = int(input())

print(chunked(txt, num))