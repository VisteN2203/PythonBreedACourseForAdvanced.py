from functools import reduce
a, b = int(input()), int(input())
list_num_one = [int(i) for i in range(a, b + 1) if "0" not in str(i)]
list_num_two = [[int(j) for j in str(i)] for i in range(a, b + 1) if "0" not in str(i)]

maps = list(map(lambda x,y: x%y == 0, list_num_one, map(lambda x: i for i in list_num_two)))

print(maps)