Timur, Ruslan = str(input()), str(input())

game_rule_one = ["ножницы", "бумага", "камень"]

Timur_hand = game_rule_one.index(Timur)
Ruslan_hand = game_rule_one.index(Ruslan)

if (Timur_hand == 2 or Timur_hand == 0) and (Ruslan_hand == 0 or Ruslan_hand == 2) and Ruslan_hand != Timur_hand:
	game_rule_one.reverse()
	Timur_hand = game_rule_one.index(Timur)
	Ruslan_hand = game_rule_one.index(Ruslan)

if Timur_hand == Ruslan_hand:
	print("ничья")
elif Timur_hand < Ruslan_hand:
	print("Тимур")
else:
	print("Руслан")

