r = "37"

(p1, p2) = 0, 1

t=768071
res="92510"
#res="01245"
fin = False
for i in range(t+10):
	#combine
	c = str(int(r[p1]) + int(r[p2]))
	for j in c:
		r += j
		if(res in r[-len(res):]):
			print(i)
			fin = True

	p1 = (p1 + 1 + int(r[p1])) % len(r)
	p2 = (p2 + 1 + int(r[p2])) % len(r)
	print(i, r)
	print(r[-len(res):])
#	print(p1, p2)
	if (fin):
		break

print(r[t:t+10])
