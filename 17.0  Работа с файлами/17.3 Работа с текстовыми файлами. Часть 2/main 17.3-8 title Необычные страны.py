dict_country = dict()

with open("../Files/population.txt", "r") as file:
	filer = file.readlines()
	for line in filer:
		dict_country[line.split("\t")[0]] = int(line.split("\t")[1][:-1])

	list_country = []
	for key, value in dict_country.items():
		if key[0] == "G" and value >= 500000:
			list_country.append(key)

	print(*list_country, sep="\n")