serial = 4172

x_g = 0
y_g = 0
v_g = 0

for x in range(1, 297):
	for y in range(1, 297):
		grid_val = 0
		for i in range(3):
			for j in range(3):
				rack_id = x+i+10
				power_level = (y+j)*rack_id
				power_level += serial
				power_level *= rack_id
				power_level = (power_level//100)%10
				power_level -= 5
				grid_val += power_level
		if (grid_val > v_g):
			x_g = x
			y_g = y
			v_g = grid_val
print("part1")
print("{},{}".format(x_g, y_g))


x_g = 0
y_g = 0
v_g = 0

for x in range(1, 300):
	for y in range(1, 300):
		grid_val = {}
		for i in range(x, 300):
			for j in range(y, 300):
				rack_id = x+i+10
				power_level = (y+j)*rack_id
				power_level += serial
				power_level *= rack_id
				power_level = (power_level//100)%10
				power_level -= 5

			y_g = y
			v_g = grid_val
print("part2")
print("{},{}".format(x_g, y_g))


