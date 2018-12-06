d_org = open("data/d5.txt").read()[:-1]
#d_org = "dabAcCaCBAcCcaDA"
sol = {}
for l in "abcdefghijklmnopqrstuvwxyz":
	d = d_org.replace(l,"").replace(l.upper(),"")

	while(True):
		stop = True
		for i in range(len(d)-1):
			x = ord(d[i])
			y = ord(d[i+1])
			diff = abs(x - y)
			if (diff == 32):
				d = d[0:i] + d[i+2:]
				stop = False
				break
		if (stop):
			break
	sol[l] = len(d)
	print(l, len(d))
print(min(sol.items(), key=lambda x : x[1]))
