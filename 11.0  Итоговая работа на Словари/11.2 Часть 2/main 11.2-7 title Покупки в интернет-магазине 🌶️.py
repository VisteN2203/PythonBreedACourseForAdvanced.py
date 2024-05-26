dict_name_products = {}

for _ in range(int(input())):
	name, product, count = str(input()).split()
	dict_name_products.setdefault(name,{})
	dict_name_products[name][product] = dict_name_products[name].get(product,0) + int(count)

for key,value in sorted(dict_name_products.items()):
	print(key + ":")
	for key_product, value_product in sorted(value.items()):
		print(key_product, value_product)