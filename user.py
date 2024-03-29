import pickle
from time import sleep, ctime

while True:
	user_id = input("Введите номер счета\n")
	with open("data_money", "rb") as fd:
		data = pickle.load(fd)
	if user_id not in data or user_id == "limit":
		print("_____________________\nНеправильный номер\n_____________________\n")
		sleep(3)
		continue
	print("Вы вошли под аккаунтом " + user_id + "\n")
	while True:
		with open("data_money", "rb") as fd:
			data = pickle.load(fd)
		print("Ваш баланс = " + str(data[user_id]) + '\n')
		user_input = input("Что хотите сделать?\n1 - Перевести на другой счёт\n2 - Обновить данные\n3 - Выйти\n")
		if user_input == "2":
			sleep(0.5)
			continue
		elif user_input == "1":
			user_input2 = input("Введите номер счета на который отправить деньги\n")
			if user_input2 not in data or user_id == user_input2 or user_input2 == "limit":
				print("_____________________\nНесуществующий номер счёта или свой\n_____________________\n")
				sleep(2)
				continue
			user_input3 = input("Введите положительное целое число, которое хотите перевести\n")
			try:
				user_input3 = int(user_input3)
			except:
				print("_____________________\nСумма указана некорретно\n_____________________\n")
				sleep(2)
				continue
			if user_input3 <= 0:
				print("_____________________\nСумма должна быть положительным числом\n_____________________\n")
				sleep(2)
				continue
			with open("data_money", "rb") as fd:
				data = pickle.load(fd)
			if data[user_id] - user_input3 < 0:
				print("_____________________\nУ вас недостаточно денег для перевода\n_____________________\n")
				continue
			if data["limit"] != None and (data[user_input2] + user_input3) >= data["limit"]:
				print("_____________________\nВы не можете перевести на этот счёт такую сумму\n_____________________\n")
				sleep(0.5)
				continue
			data[user_id] -= user_input3
			data[user_input2] += user_input3
			with open("data_money", "wb") as fd:
				pickle.dump(data, fd)
			with open("log.txt", "a") as fd:
				fd.write(ctime() + "    " + user_id + "  ---->   " + user_input2 + "          " + str(user_input3) + "\n")
			print("___________________\nУспешно\n___________________\n")
		elif user_input == "3":
			exit()
		else:
			print("________________________\nНеверный ввод\n________________________\n")
			sleep(1.5)
