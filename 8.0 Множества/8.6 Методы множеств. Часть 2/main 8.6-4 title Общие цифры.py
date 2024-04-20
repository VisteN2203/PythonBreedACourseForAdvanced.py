n = int(input())

set_numbers = set(input())

for i in range(1, n):
	set_numbers &= set(input())

print(*sorted(set_numbers))
