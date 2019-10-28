# -*- coding: utf-8 -*-
import pickle

while True:
	with open("data_money", "rb") as fd:
		data = pickle.load(fd)
	print(" ID  ----------  BANK ACCOUNT VALUE")
	for i in data:
		print(i + "  ----------  " + str(data[i]))
	user_input = input("Что хотите сделать?\n1 - работа со счётом\n2 - обновить данные\n3 - установить лимит\n4 - Выход\n")
	if user_input == '2':
		continue
	elif user_input == '4':
		exit()
	elif user_input == '1':
		user_input2 = input("Введите номер счёта\n")
		try:
			user_input3 = int(input("Введите положительное целое число, если хотите увеличить баланс.\nИли отрицательное целое, если уменьшить\n"))
		except:
			print("_______________________\nНужно было только число\n________________________")
		if user_input2 in data and user_input2 != "limit":
			data[user_input2] += user_input3
			with open("data_money", "wb") as fd:
				pickle.dump(data, fd)
		else:
			print("________________________________\nНеправильно введён номер счёта\n________________________________")
	elif user_input == "3":
		user_input2 = input("""Введите число, выше которого нельзя будет перечислить на счёт\nЧисло может быть и не положительным
Если хотите убрать лимит, введите \'no\' \n""")
		if user_input2.lower() in ["no", "n"]:
			data["limit"] = None
			with open("data_money", "wb") as fd:
				pickle.dump(data, fd)
		else:
			try:
				user_input2 = int(user_input2)
			except:
				continue
			data["limit"] = user_input2
			with open("data_money", "wb") as fd:
				pickle.dump(data, fd)
