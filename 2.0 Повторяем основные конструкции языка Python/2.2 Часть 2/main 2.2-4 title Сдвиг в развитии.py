list_num = [str(number) for number in str(input()).split()]

delete_num = list_num.pop(len(list_num) - 1)
list_num.insert(0, delete_num)
print(*list_num)
