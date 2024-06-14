def matrix(num_one, num_two, num_three):
    list = [[num_three * num_two] for _ in range(num_one)]
    return list


num_one, num_two, num_three = input(), input(), input()

if num_one == '':
    num_one = 1

if num_two == '':
    num_two = num_one

if num_three == '':
    num_three = 0

print(matrix(int(num_one),int(num_two),int(num_three)))