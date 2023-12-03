filename = "input3.txt"

def solution3():
     
	with open(filename) as f:
		content = f.readlines()

	foundNumbers = []
	sum = 0

	output = ""

	for i in range(len(content)):
		j = 0
		while j in range(len(content[i])):
			if (content[i][j].isdigit()):
				line = i
				number = ""
				indexesOnLine = []

				#the idea is to find the indexes of the numbers and then everything neighbouring these indexes
				while True:
					if content[i][j].isdigit():
						number += content[i][j]
						indexesOnLine.append(j)
						if not j + 1 > len(content[i]) - 1 and content[i][j + 1].isdigit():
							j += 1
						else: break

				lineIndexStart = i - 1
				lineIndexEnd = lineIndexStart + 3
				if lineIndexStart < 0:
					lineIndexStart = 0
				if lineIndexEnd > len(content) - 1:
					lineIndexEnd = len(content) - 1

				charIndexStart = indexesOnLine[0] - 1
				charIndexEnd = charIndexStart + len(indexesOnLine) + 2
				if charIndexStart < 0:
					charIndexStart = 0
				if charIndexEnd > len(content[i]) - 1:
					charIndexEnd = len(content[i]) - 1

				numberIsFound = False
				for k in range(lineIndexStart, lineIndexEnd):
					for l in range(charIndexStart, charIndexEnd):
						if not content[k][l] == "." and not content[k][l].isdigit():
							foundNumbers.append(number)
							numberIsFound = True
							break
					if numberIsFound:
						break

			j += 1 
	
	for element in foundNumbers:
		sum += int(element)
		print(element)
	
	print(sum)

def main():
    solution3()  

if __name__ == "__main__":
    main()