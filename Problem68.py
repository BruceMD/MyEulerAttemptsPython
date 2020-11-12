from itertools import permutations

def main():
	
	lis = [i for i in range(1, 11)]
	
	validGong = []
	
	for lim in range(14, 20):
		for perm in permutations(lis, 5):
#			print(perm)
			check = True
			invPerm = invLis(perm)
			for j in range(-1, 4):
				num = lim - perm[j] - perm[j+1]
				if num in invPerm:
					invPerm.remove(num)
				else:
					check = False
					break
			if check:
				validGong.append(printGonRing(perm, lim))
			
	findMax(validGong)
			

def findMax(rings):
	tempMax = 0
	
	


def funFun(gonRing):
	localMax = 0
	side1, side2, side3, side4, side5 = [0, 6, 7], [1, 7, 8], [2, 8, 9], [3, 9, 5], [4, 5, 6]
	gonRingColl = [side1, side2, side3, side4, side5]

	for i in range(-1, 4):
		
	
	

def convertToNum(x):
	None


def printGonRing(perm, lim):
	lis = [None]*10
	n = 5
	for p in perm:
		lis[n] = p
		n += 1
	ref = [[6, 7], [7, 8], [8, 9], [9, 5], [5, 6]]
	for k in range(5):
		lis[k] = lim - lis[ref[k][0]] - lis[ref[k][1]]
	print(lis)
	return lis


def invLis(p):
	invLis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for n in p:
		if n in invLis:
			invLis.remove(n)
	return invLis
	
if __name__ == '__main__':
	main()
