translate_dict = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }

with open("../Files/cyrillic.txt","r",encoding="utf-8") as old_text:
	with open("../Files/transliteration.txt","w",encoding="utf-8") as new_text:
		for i in old_text.read():
			if i in translate_dict:
				new_text.write(translate_dict[i])
			elif i.lower() in translate_dict:
				new_text.write(translate_dict[i.lower()].capitalize())
			else:
				new_text.write(i)
