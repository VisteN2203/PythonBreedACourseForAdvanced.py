import random

word = str(input())

list_num = [i for i in range(len(word))]
random.shuffle(list_num)

for num_letter in list_num:
    print(word[num_letter],end="")

