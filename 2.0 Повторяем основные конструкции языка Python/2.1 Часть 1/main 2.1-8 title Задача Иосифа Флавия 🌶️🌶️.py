n, k = int(input()), int(input())

s = [i for i in range(1, n + 1)]

while len(s) > 1:
	for q in range(0,k-1):
		s.append(s[q])
	del s[:k]
print(s)