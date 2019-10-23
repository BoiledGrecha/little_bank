import pickle

data = {"001" : 100,
		"020" : 999,
		"100" : 5,
		"150" : 500,
		"300" : 1000,
		"666" : 100000,
		"limit" : None}

with open("data_money", "wb") as fd:
	pickle.dump(data, fd)

with open("data_money", "rb") as fd:
	data2 = pickle.load(fd)

print(data2)
