data = open("data/d4.txt", "r").read().split("\n")[:-1]

for record in data:
	record = record.split(" ")
	time = record[1]
	print (time)
