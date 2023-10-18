options = ["ножницы", "бумага", "камень", "ящерица", "Спок"]

timur_move = input()
ruslan_move = input()

timur_option = options.index(timur_move)
ruslan_option = options.index(ruslan_move)
result = timur_option - ruslan_option
if ruslan_option == timur_option:
	print("ничья")
elif result % 2 == 0:
	if timur_option < ruslan_option:
		print("Руслан")
	else:
		print("Тимур")
elif result % 2 != 0:
	if timur_option > ruslan_option:
		print("Руслан")
	else:
		print("Тимур")
