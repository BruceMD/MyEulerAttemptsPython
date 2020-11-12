def main():
	
	lis = [i for i in range(1, 11)]
	for lim in range(14, 20):
		rec([], lis, lim)
	
	
	
def rec(gonRing, lis, lim):
	if (len(gonRing) == 10) and (0 not in gonRing):
		print(gonRing)
		return
	
	side1, side2, side3, side4, side5 = [0, 6, 7], [1, 7, 8], [2, 8, 9], [3, 9, 5], [4, 5, 6]
	gonRingColl = [side1, side2, side3, side4, side5]
	
	for num in lis:
		ind = len(gonRing)
		numSides = []						# get the triangles associated with that index
		for side in gonRingColl:
			if ind in side:
				numSides.append(side)
		check = True
		for side in numSides:
			if sumSide(gonRing, side) + num == lim 
		

def lenSide(gonRing, sideLis):
	count = 0
	for n in sideLis:
		if n < len(gonRing):
			count += 1
	return count


def sumSide(gonRing, sideLis):
	total = 0
	for n in sideLis:
		if n < len(gonRing):
			total += gonRing[n]
	
	return total


if __name__ == '__main__':
	main()
