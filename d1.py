data = open("data/d1.txt", "r").read().split("\n")[:-1]
#data = ["+7", "+7", "-2", "-7", "-4"]
seen ={0}
size = len(data)
res = 0
pos = 0

while(True):
	val = data[pos]
	if (val[0] is "-"):
		res -= int(val[1:])
	else:
		res += int(val[1:])
	if (res in seen):
		print(res)
		break
	pos += 1
	if (pos == size):
		pos = 0
	seen.add(res)
