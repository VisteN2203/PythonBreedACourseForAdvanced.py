number = int(input())

set_letter = set()

for _ in range(number):
	word = input().lower()
	for i in word:
		set_letter.add(i)

print(len(set_letter))