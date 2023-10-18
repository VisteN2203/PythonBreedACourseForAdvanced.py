new_text = str(input()) + " " + "запретил букву"
list_text = [letter for letter in new_text]

letters, list_del = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
		   'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'], []

print(f"{new_text} {letters[0]}")
for i in range(0,len(letters)):
	old_word, new_word = "".join(list_text), ""
	if old_word.find(letters[i]) > -1:
		for j in range(0, len(list_text)):
			if letters[i] != list_text[j]:
				new_word += list_text[j]
			else:
				list_del.append(j)
		for z in range(len(new_word)-1):
			if new_word[z] == " " and new_word[z+1] == " ":
				new_word = new_word[:z] + new_word[z+1:]
		for k in range(i,len(letters)-1):
			if old_word.find(letters[k + 1]) > -1:
				print(new_word.strip() + " " + str(letters[k + 1]))
				break
		nums = 0
		for n in range(len(list_del)):
			list_text.pop(list_del[n] - nums)
			nums += 1
		list_del = []
