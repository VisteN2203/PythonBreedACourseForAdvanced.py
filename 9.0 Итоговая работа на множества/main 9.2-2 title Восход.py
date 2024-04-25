num = str(input())

num_list = num.split()

num_step = {i for i in num_list}

print(len(num_list) - len(num_step))