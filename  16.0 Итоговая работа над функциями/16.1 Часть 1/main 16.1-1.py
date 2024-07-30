def generate_letter(mail, name, date, time, place, teacher = "Тимур Гуев", number = 17):
	list = [f"To: {mail}",
			f"Приветствую, {name}!",
			f"Вам назначен экзамен, который пройдет {date}, в {time}.",
			f"По адресу: {place}.",
			f"Экзамен будет проводить {teacher} в кабинете {number}.",
			f"Желаем удачи на экзамене!"]
	return f"To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!"


print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))

