import numpy as np

data = open("data/d3.txt", "r").read().split("\n")[:-1]


grid = np.full((1000,1000), 0)
#grid = np.full((8,8), 0)
#print(grid)

#print(grid[1][1])

#data = ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]

IDs = set()
for claim in data:
	claim = claim.split(" ")
#	print(claim)
	id = int(claim[0].replace("#",""))
	IDs.add(id)
#	print(id)
	x, y = map(int, claim[2].replace(":","").split(","))
	w, h = map(int, claim[3].split("x"))
#	print(x,y,w,h)
	for i in range(y,y+h):
		for j in range(x, x+w):
			if (grid[i][j] == 0):
				grid[i][j] = id
			else:
				IDs.discard(grid[i][j])
				IDs.discard(id)
				grid[i][j] = id
				overlapCounter += 1
				
				
	
#print(grid)	
print(overlapCounter)
print(IDs)
	
