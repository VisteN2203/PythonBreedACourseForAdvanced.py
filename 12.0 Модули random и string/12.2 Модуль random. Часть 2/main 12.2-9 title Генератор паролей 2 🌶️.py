import random
import string
def generate_password(length):
	upper_case = [i for i in string.ascii_uppercase if i not in "IO"]
	lower_case = [i for i in string.ascii_lowercase if i not in "lo"]
	digits = list(string.digits[2:])
	chars = upper_case + lower_case + digits

	result = [random.choice(i) for i in (upper_case, lower_case, digits)]
	result += [random.choice(chars) for _ in range(length - 3)]

	return "".join(result)
def generate_passwords(count, length):
	return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())

print(*generate_passwords(n,m), sep="\n")

