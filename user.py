import pickle
from time import sleep

while True:
	user_id = input("Введите номер счета\n")
	with open("data_money", "rb") as fd:
		data = pickle.load(fd)
	if user_id not in data:
		print("_____________________\nНеправильный номер\n_____________________\n")
		sleep(3)
		continue
	print("Вы вошли под аккаунтом " + user_id + "\n")
	while True:
		with open("data_money", "rb") as fd:
			data = pickle.load(fd)
		print("Ваш баланс = " + str(data[user_id]) + '\n')
		user_input = input("Что хотите сделать?\n1 - Перевести на другой счёт\n2 - Обновить данные\n")
		if user_input == "2":
			sleep(0.5)
			continue
		elif user_input == "1":
			# ввести номер на который кинуть, потом сколько скинуть
			# сверить что не превысит, иначе вернуть
			exit()
