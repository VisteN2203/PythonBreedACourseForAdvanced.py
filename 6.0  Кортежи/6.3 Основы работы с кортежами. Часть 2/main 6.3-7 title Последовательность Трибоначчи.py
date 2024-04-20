num = int(input())
class_tuple = (1, 1, 1)
listic = []

for i in class_tuple:
	listic.append(i)


for k in range(2,num):
	listic.append(listic[k-2] + listic[k-1] + listic[k])


for j in range(0, num):
	print(listic[j], end=" ")