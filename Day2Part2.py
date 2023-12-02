filename = "input2.txt"

def solution2():
    
	sumOfPowers = 0
	

	with open(filename) as f:
		content = f.readlines()

	for line in content:

		minCounts = {
			"red" : 0,
			"green" : 0,
			"blue" : 0,
		}

		noSpaces = line.replace(" ", "")
		splitLine = noSpaces.split(":")
		valueString = splitLine[1]
		sets = valueString.split(";")

		for set in sets:

			countsDict = {
			"red" : 0,
			"green" : 0,
			"blue" : 0,
			}

			values = set.split(",")

			for value in values:
				number = ""
				i = 0

				while value[i].isdigit():
					number += value[i]
					i += 1



				if "red" in value:
					countsDict["red"] += int(number)
				elif "green" in value:
					countsDict["green"] += int(number)
				else:
					countsDict["blue"] += int(number)
			

			for element in countsDict:
				if countsDict[element] > minCounts[element]:
					minCounts[element] = countsDict[element]
		
		
		activeSum = 1
		for element in minCounts:
			activeSum *= minCounts[element]

		sumOfPowers += activeSum
	print(sumOfPowers)

def main():
    solution2()  

if __name__ == "__main__":
    main()