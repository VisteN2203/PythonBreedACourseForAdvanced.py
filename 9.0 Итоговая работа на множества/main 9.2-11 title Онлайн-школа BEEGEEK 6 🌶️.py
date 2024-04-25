n = int(input())

second_lesson = {str(input()) for i in range(int(input()))}
if n > 1 :
	for j in range(n-1):
		second_lesson &= {str(input()) for j in range(int(input()))}

print(*sorted(second_lesson),sep="\n")