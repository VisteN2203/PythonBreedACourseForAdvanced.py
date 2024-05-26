emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

list_emails = []
for key, value in emails.items():
	for username in value:
		list_emails.append(username + "@" + key)

for i in sorted(list_emails):
	print(i)