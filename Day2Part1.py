filename = "input2.txt"

def solution2():
     
	cubeCount = {
		"red" : 12,
		"green" : 13,
		"blue" : 14,
	}
    
	possibleIDs = []
	sumOfPossibleGames = 0

	with open(filename) as f:
		content = f.readlines()

	for line in content:

		noSpaces = line.replace(" ", "")
		splitLine = noSpaces.split(":")
		valueString = splitLine[1]
		sets = valueString.split(";")

		possibleGame = True

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
				if countsDict[element] > cubeCount[element]:
					possibleGame = False
					break

		if possibleGame == True:
			gameID = ""
			for char in splitLine[0]:
				if char.isdigit():
					gameID += char

			possibleIDs.append(gameID)
				

	for gameID in possibleIDs:
		print(gameID)
		sumOfPossibleGames += int(gameID)

	print(sumOfPossibleGames)

def main():
    solution2()  

if __name__ == "__main__":
    main()