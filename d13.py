data = open("data/d13.txt","r").read().split("\n")[:-1]

for i in range(len(data)):
	print(data[i])

trains =[]

for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] in "<>v^":
			print("found player", i, j)
			trains.append((i,j, 0))


print(trains)
