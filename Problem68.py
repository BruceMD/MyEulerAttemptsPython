from itertools import permutations

def main():
	
	lis = [i for i in range(1, 11)]
	
	validGong = []					# put all perms that make 5 gon rings here
	
	for lim in range(14, 20):
		for perm in permutations(lis, 5):
									# Explore all permutations of 5 numbers that make up the inner core -> perm(1:10, 5)
			check = True
			invPerm = invLis(perm)
			for j in range(-1, 4):
				num = lim - perm[j] - perm[j+1]
				if num in invPerm:			# Then matched the remaining five to where they could go
					invPerm.remove(num)
				else:
					check = False			# If there was a conflict then I'd quit this perm and move to the next option
					break
			if check:					# No conflicts, then send to printGonRing to order them correctly
				validGong.append(printGonRing(perm, lim))
			
	print(findMax(restrict(validGong)))

	
def restrict(rings):						# only allow cases where 10 is in the external nodes (index 0:4)
	newRingList = []
	
	for ring in rings:
		if 10 in ring[0:5]:
			newRingList.append(ring)
	return newRingList

	
def findMax(rings):							# Go through each ring and see which is the largest
	tempMax = 0
	
	for ring in rings:
		num = localMax(ring)
		if num > tempMax:
			tempMax = num
			
	return tempMax


def localMax(gonRing):
	# need to keep cyclical order important within each side, but because it is cyclical, we can choose where to start
	side1, side2, side3, side4, side5 = [0, 6, 7], [1, 7, 8], [2, 8, 9], [3, 9, 5], [4, 5, 6]
	gonRingColl = [side1, side2, side3, side4, side5]
								# list of lists because sequence is not important to a dictionary

	i = startInd(gonRing)					# starting from the lowest external node

	tempNum = ""
	for j in fivePerm(i):					# go through each side starting at i
		for k in gonRingColl[j]:			# add each number from each side
			tempNum += str(gonRing[k])		# there seemed to be something wrong with tempNum += tempNum*10 + gonRIng[k]
								# so I converted to a string, put them together and converted back to a integer

	return int(tempNum)


def startInd(ring):						# choose min from the first 5 numbers - external nodes
	return ring.index(min(ring[0:5]))


def fivePerm(x):						# find the index of starting min external node and travel in a circle from here
	fiveLis = []
	for h in range(x, x+5):
		if h > 4:
			fiveLis.append(h-5)
		else:
			fiveLis.append(h)
	
	return fiveLis


def printGonRing(perm, lim):
	lis = [None]*10
	n = 5
# five EXTERNAL nodes are 0:4
# five inner noces are at 5:9
	for p in perm:
		lis[n] = p
		n += 1
	ref = [[6, 7], [7, 8], [8, 9], [9, 5], [5, 6]]
	for k in range(5):
		lis[k] = lim - lis[ref[k][0]] - lis[ref[k][1]]
	print(lis)
	return lis


def invLis(p):								# whatever is in p will not be in invLis, pretty self explanatory
	invLis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for n in p:
		if n in invLis:
			invLis.remove(n)
	return invLis
	
if __name__ == '__main__':
	main()
