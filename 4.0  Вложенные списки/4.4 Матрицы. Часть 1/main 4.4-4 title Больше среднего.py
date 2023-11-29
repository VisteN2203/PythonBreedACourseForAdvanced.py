n,list, sum , list_two = int(input()), [] ,0 , []

[list.append(str(input()).split()) for k in range(n)]

for i in range(n):
    for j in range(n):
        sum += int(list[i][j])
    list_two.append(sum / n)
    sum = 0

total = 0
for l in range(n):
    for h in range(n):
        if float(list[l][h]) > int(list_two[l]):
            total += 1

    print(total)
    total = 0


