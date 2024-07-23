set_correct = set()
list_all_nicknames = []
num = int(input())

def rounded(num):
	float_num = 100 / num * len(list_all_nicknames)
	if float_num - int(float_num) >= 0.5:
		return int(float_num) + 1
	else:
		return int(float_num)

for i in range(num):
	nickname, result_answer = input().split(": ")
	if result_answer == "Correct":
		set_correct.add(nickname)
		list_all_nicknames.append(nickname)


if len(set_correct) >= 1:
	print(f"Верно решили {len(set_correct)} учащихся")
	print(f"Из всех попыток {rounded(num)}% верных")
else:
	print("Вы можете стать первым, кто решит эту задачу")
