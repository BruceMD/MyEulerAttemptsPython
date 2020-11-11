def main():
	
	gonRing = []
	
	side1 = [0, 6, 7]
	side2 = [1, 7, 8]
	side3 = [2, 8, 9]
	side4 = [3, 9, 5]
	side5 = [4, 5, 6]
	gonRingColl = [side1, side2, side3, side4, side5]
	
	lis = [i for i in range(1, 11)]
	for lim in range(14, 20):
		rec(gonRing, lis, lim)
	
	
	
def rec(gonRing, lis, lim):
	if (len(gonRing) == 10) and (0 not in gonRing):
		print(gonRing)
		return
	
	side1 = [0, 6, 7]
	side2 = [1, 7, 8]
	side3 = [2, 8, 9]
	side4 = [3, 9, 5]
	side5 = [4, 5, 6]
	gonRingColl = [side1, side2, side3, side4, side5]
	
	for num in lis:
		ind = len(gonRing)
		for side in gonRingColl:
			if ind in side:
				if (len(side) < 2 and sum(side) + num < lim):
					



def checkLine(line, limit):
	return sum(line) == limit and len(line) == 3
	
if __name__ == '__main__':
	main()
