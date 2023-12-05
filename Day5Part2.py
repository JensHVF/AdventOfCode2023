filename = "input5.txt"

def solution5():
	with open(filename) as f:
		content = f.read()

	splitFile = content.split("\n\n")
      
	seedsRanges = splitFile[0].replace("seeds: ", "").split(" ")
    
	seeds = []
	newSeeds = []

	for i in range(0, len(seedsRanges), 2):
		seedsRange = []
		seedsRange.append(int(seedsRanges[i]))
		seedsRange.append(int(seedsRanges[i]) + (int(seedsRanges[i + 1]) - 1))
		seeds.append(seedsRange)

	maps = []
      
	for i in range(1, len(splitFile)):
		splitMap = splitFile[i].split(":")
		maps.append(splitMap[1])


	allExtremesInfo = []

	currentInfoIndex = 0

	for i in range(len(seeds)):
		for j in range(len(seeds[i])):
			seedInfo = []

			currentInfo = int(seeds[i][j])

			seedInfo.append(currentInfo)

			for map in maps:

				lineValues = map.split("\n")
				lineValues.remove('')
				for values in lineValues:
					splitValues = values.split(" ")

					conversionStart = int(splitValues[0])
					rangeStart = int(splitValues[1])
					valueRange = int(splitValues[2])



					if (currentInfo <= rangeStart + (valueRange - 1) and currentInfo >= rangeStart):

						if not j + 1 > 1 and int(seeds[i][j + 1]) > rangeStart + (valueRange - 1):
							rangeMax = int(seeds[i][j + 1])

							seeds[i][j + 1] = int(seeds[i][j]) + (valueRange - 1)

							# rangeMax - (rangeStart + (valueRange - 1))
							newSeeds.append([int(seeds[i][j + 1]) + 1, rangeMax])

						currentInfo = conversionStart + (currentInfo - rangeStart)
						break

				seedInfo.append(currentInfo)

			allExtremesInfo.append(seedInfo)

	for i in range(len(newSeeds)):
		for j in range(len(newSeeds[i])):
			seedInfo = []

			currentInfo = int(newSeeds[i][j])

			seedInfo.append(currentInfo)

			for map in maps:

				lineValues = map.split("\n")
				lineValues.remove('')
				for values in lineValues:
					splitValues = values.split(" ")

					conversionStart = int(splitValues[0])
					rangeStart = int(splitValues[1])
					valueRange = int(splitValues[2])



					if (currentInfo <= rangeStart + (valueRange - 1) and currentInfo >= rangeStart):
						currentInfo = conversionStart + (currentInfo - rangeStart)
						break

				seedInfo.append(currentInfo)

			allExtremesInfo.append(seedInfo)

	lowest = 0

	for info in allExtremesInfo:
		if lowest == 0:
			lowest = info[7]
		elif info[7] < lowest:
			lowest = info[7]

	print(lowest)

def main():
    solution5()  

if __name__ == "__main__":
    main()