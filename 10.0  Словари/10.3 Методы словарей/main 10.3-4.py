string_list = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'


# s = string_list.split()
# my_dict = {}
#
# for i in s:
# 	my_dict[i] = s.count(i)
#
# result = {}
# max_count = max(my_dict.values())
#
# for key, value in my_dict.items():
# 	if value == max_count:
# 		result[key] = value
#
# print(min(result))

string_list = string_list.split()
dict_word = dict()

for word in string_list:
	dict_word[word] = dict_word.get(word,0) + 1

list_max_word = []
for key, value in dict_word.items():
	if value == max(dict_word.values()):
		list_max_word.append(key)

print(min(list_max_word))

