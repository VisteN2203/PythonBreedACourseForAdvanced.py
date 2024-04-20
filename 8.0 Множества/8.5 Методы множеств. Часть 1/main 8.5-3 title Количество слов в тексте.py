text = [i.lower().strip('.,;:-?!') for i in input().split()]

set_text = set()
for j in text:
	set_text.add(j)

print(len(set_text))