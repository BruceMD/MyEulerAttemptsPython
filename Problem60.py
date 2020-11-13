from itertools import permutations
from typing import List


def main():
	listP = genPrimeSix()
	listPAll = listP + genPrimeSeven()

# let's test all the permutations of prime numbers going up to 100 000. Fortunately, we will start using 3 and 70
	for perm in permutations(listP, 5):
		check = True
		for perTwo in permutations(perm, 2):
			p1, p2 = concatenate(perTwo[0], perTwo[1])
			if p1 not in listP or p2 not in listPAll:
				check = False
				break
		if check:
			print(sum(perm))
			print(perm)
			break


def concatenate(a, b):
	c = int(str(a) + str(b))
	d = int(str(b) + str(a))

	return c, d


def genPrimeSix():
	listP = []

	for i in range(3, 100000, 2):
		if isPrime(i):
			listP.append(i)

	return listP


def genPrimeSeven():
	listPSeven = []

	for i in range(100001, 1000000, 2):
		if isPrime(i):
			listPSeven.append(i)

	return listPSeven


def isPrime(x):
	count = 0
	for i in range(3, round(x ** 0.5) + 1, 2):
		if x % i == 0:
			count += 1
			return False
			break
	if count == 0:
		return True


if __name__ == "__main__":
	main()