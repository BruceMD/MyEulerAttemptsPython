def main():

	# Commit 1
	# quick roman numerals to decimal system converter
	# not over the moon with the open() function that stores all my data in my code into lis
	# then processes all the data, would be smarter to handle each line from 'p089_roman.txt'
	# instead of saving each file but this is only 1000 lines long so not the end of the world
	
	# Commit 2
	
	originalLen = genDecimals() 
	updateLen = genRoman())
	
	# Commit 3 to get the lengths differences
	print(originalLen - updateLen)
	
	
def genRoman():
	lis = []
	with open("RomanToDecimals.txt", "r") as file:
		for item in file.readlines():
			lis.append(item.strip("\n"))
#	print(lis)
	
	libRef = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	lib = {1000: "M", 900: "CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
	
	newFile = open("DecimalToRoman.txt", "w")
	DTRCount = 0
	
	for number in lis:
		n = 0
		decimalNum = int(number)
		romanNum = ""
		while decimalNum > 0:
			if decimalNum >= libRef[n]:
				decimalNum -= libRef[n]
				romanNum += lib[libRef[n]]
			else:
				n += 1
		DTRCount += len(romanNum)
		newFile.write(romanNum + "\n")

	newFile.close()
	return DTRCount

def genDecimals():
	lis = []
	with open('p089_roman.txt', 'r') as file:
		for item in file.readlines():
			lis.append(item.strip("\n"))
			
#	print(lis)
	p089Count = 0
	
	newFile = open("RomanToDecimals.txt", "w")
	
	romanN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	
	for number in lis:
		numberValue = 0
		podium = 0
		mem = "M"
		for digit in number:
			p089Count += 1
			if check(mem, digit):
				numberValue += podium
				podium, mem = romanN[digit], digit
			else:
				podium = romanN[digit] - podium
		numberValue += podium
		newFile.write(str(numberValue) + "\n")
	
	newFile.close()
	
	return p089Count
	
def check(a, b):

	lib = {"M":6, "D":5, "C":4, "L":3, "X":2, "V":1, "I":0}
	
	if lib[b] > lib[a]:
		return False
	return True
	
	
	
if __name__ == '__main__':
	main()
