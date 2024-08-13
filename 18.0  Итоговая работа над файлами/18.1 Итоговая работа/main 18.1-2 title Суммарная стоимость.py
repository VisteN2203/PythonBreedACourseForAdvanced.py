with open("../Files/ledger.txt","r", encoding="utf-8") as file:
	result = list()
	for line in file.readlines():
		result.append(int(line[1:].replace("\n","")))
	print(f"${sum(result)}")