list_numbers = [str(input()) for i in range(int(input()))]

def ip_number_in_ten(ip_number):
	total = 0
	list_numbers_new = [int(i) for i in ip_number.split(".")]
	list_numbers_new.reverse()
	for i in range(0,4):
		total += list_numbers_new[i] * pow(255,i)
	return total

print(*sorted(list_numbers, key= lambda x: ip_number_in_ten(x)), sep="\n")
