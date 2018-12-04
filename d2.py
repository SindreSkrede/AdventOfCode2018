data = open("data/d2.txt", "r").read().split("\n")[:-1]

#data = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

twoCount = 0
threeCount = 0

for ID in data:
	letters = {}
	for l in ID:
		if (l not in letters):
			letters[l] = 1
		else:
			letters[l] += 1
	if (2 in letters.values()):
		twoCount += 1
	if (3 in letters.values()):
		threeCount += 1
print(twoCount * threeCount) 

for ID in data:
	for ID2 in data:
		diff = 0
		diffpos = 0
		for i in range(min(len(ID), len(ID2))):
			if (ID[i] != ID2[i]):
				diff += 1
				diffpos = i
		if(diff == 1):
			print(ID[0:diffpos] + ID[diffpos+1:])

