d = open("data/d7.txt", "r").read().split("\n")[:-1]

graph = {}

for i in d:
	#print(i)
	#print(i[5])
	t  = i[5]
	d = i[36]
	#print(i[36])
	if (t not in graph):
		graph[t] = set()
	if (d not in graph):
		graph[d] = {t}
	else:
		graph[d].add(t)

#for i in graph:
#	print(i, graph[i])
sol = ""
#while(len(grap) > 0):

while(True):
	for i in graph:
		print(i, graph[i])
	e = sorted([x for x in graph.items() if x[1] == set()])
	print(e)
	if(len(e) == 0):
		break
	e = e[0]
	sol += e[0]
	graph.pop(e[0],None)
	for i in graph:
		graph[i].discard(e[0])

print(sol)
	


