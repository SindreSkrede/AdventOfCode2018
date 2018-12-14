data = open("data/d6.txt","r").read().split("\n")[:-1]

grid = []
for i in range(100):
	grid.append([])
	for j in range(100):
		grid[i].append('.')


for i in range(len(grid)):
	for j in range(len(grid[i])):
		print(grid[i][j], end="")
	print()
