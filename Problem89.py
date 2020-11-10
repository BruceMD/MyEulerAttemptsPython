def main():

	# quick roman numerals to decimal system converter
	# not over the moon with the open() function that stores all my data in my code into lis
	# then processes all the data, would be smarter to handle each line from 'p089_roman.txt'
	# instead of saving each file but this is only 1000 lines long so not the end of the world


	lis = []
	with open('p089_roman.txt', 'r') as file:
		n = 1
		for item in file.readlines():
			n += 1
			lis.append(item.strip("\n"))
			
	print(lis)
	
	newFile = open("resultsFile.txt", "w")
	
	romanN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	
	count = 0
	for number in lis:
		numberValue = 0
		podium = 0
		mem = "M"
		for digit in number:
			count += 1
			if check(mem, digit):
				numberValue += podium
				podium, mem = romanN[digit], digit
			else:
				podium = romanN[digit] - podium
		numberValue += podium
		newFile.write(number + " >>> " + str(numberValue) + "\n")
	
	
	newFile.close()
	
def check(a, b):

	lib = {"M":6, "D":5, "C":4, "L":3, "X":2, "V":1, "I":0}
	
	if lib[b] > lib[a]:
		return False
	return True
	
	
	
if __name__ == '__main__':
	main()