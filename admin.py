# -*- coding: utf-8 -*-
import pickle
from time import sleep

while True:
	with open("data_money", "rb") as fd:
		data = pickle.load(fd)
	print(" ID  ----------  BANK ACCOUNT VALUE")
	for i in data:
		print(i + "  ----------  " + str(data[i]))
	user_input = input("Что хотите сделать?\n1 - работа со счётом\n2 - обновить данные\n3 - Выход\n")
	if user_input == '2':
		continue
	elif user_input == '3':
		exit()
	elif user_input == '1':
		user_input2 = input("Введите номер счёта\n")
		user_input3 = int(input("Введите положительное целое число, если хотите увеличить баланс.\nИли отрицательное целое, если уменьшить\n"))
		if user_input2 in data:
			data[user_input2] += user_input3
			with open("data_money", "wb") as fd:
				pickle.dump(data, fd)
		else:
			print("Неправильно введён номер счёта")
