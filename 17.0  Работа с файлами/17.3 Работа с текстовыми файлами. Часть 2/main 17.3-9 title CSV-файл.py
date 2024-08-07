def read_csv ():
	with open("../Files/data.csv") as file:
		read_file = file.readlines()

		main_list = read_file[0][:-1].split(",")

		other_list = [read_file[i][:-1].split(",") for i in range(1,len(read_file))]

		zip_list = [dict(zip(main_list, other_list[i])) for i in range(len(other_list))]

		return zip_list

print(read_csv())