import datetime

with open("../Files/logfile.txt", "r", encoding="utf-8") as file_read:
	with open("../Files/output.txt", "w", encoding="utf-8") as file_write:
		for text in file_read.readlines():
			format_string = "%H:%M"
			name, time_one, time_two = text.split(",")
			entry_time = datetime.datetime.strptime(time_one[1:], format_string)
			exit_time = datetime.datetime.strptime(str(time_two[1:]).replace("\n",""), format_string)
			if exit_time - entry_time >= datetime.timedelta(hours=1):
				file_write.write(name + "\n")



