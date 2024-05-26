text = str(input()).split(" ")

dict = dict()
for i in text:
	dict[i] = dict.get(i,0) + 1
	print(dict[i],end=" ")