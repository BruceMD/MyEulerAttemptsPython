def main():
	
	listP = [2]
	for i in range(3, 1000000, 2):
		if isPrime(i):
			listP.append(i)
	
	redFrac = []
	
	for d in range(2, 1000000):
		for n in range(1, d):
			red = reduce(n, d, listP)
			if red not in redFrac:
				redFrac.append(red)
				
	print(redFrac)
	print(len(redFrac))
	
	
def reduce(n, d, listP, ind=0):
	if n in listP or d in listP:
		return [n, d]
	
	while (listP[ind] < n):
		temp = listP[ind]
		if (n*d)%(temp**2) == 0:
			return reduce(n/temp, d/temp, listP, ind)
		else:
			ind += 1
	
	return [n, d]
	
	
def isPrime(x):
	count = 0
	for i in range(3, round(x**0.5)+1, 2):
		if x % i == 0:
			count += 1
			return False
	if count == 0:
		return True
		
	
if __name__ == "__main__":
	main()