filename = "input3.txt"

def solution3():
     
	with open(filename) as f:
		content = f.readlines()

	foundNumbers = []
	numberAndGearIndex = []
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
						if content[k][l] == "*":
							numberAndGearIndex.append([number, k, l])
					if numberIsFound:
						break

			j += 1 
	
	countedGears = []

	for a in range(0, len(numberAndGearIndex), 1):
		num = str(numberAndGearIndex[a][1]) + str(numberAndGearIndex[a][2])
		for b in range(0, len(numberAndGearIndex), 1):
			num2 = str(numberAndGearIndex[b][1]) + str(numberAndGearIndex[b][2])

			if num == num2 and numberAndGearIndex[a][0] != numberAndGearIndex[b][0] and not num in countedGears:
				countedGears.append(num)
				sum += (int(numberAndGearIndex[a][0]) * int(numberAndGearIndex[b][0]))

	print(sum)

def main():
    solution3()  

if __name__ == "__main__":
    main()