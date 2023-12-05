filename = "input5.txt"

#this doesn't actually work, i gave up, first on life and then the problem

def solution5():
	with open(filename) as f:
		content = f.read()

	splitFile = content.split("\n\n")
      
	seeds = splitFile[0].replace("seeds: ", "").split(" ")
      
	maps = []
      
	for i in range(1, len(splitFile)):
		splitMap = splitFile[i].split(":")
		maps.append(splitMap[1])

	allSeedsInfo = []

	for seed in seeds:
		
		seedInfo = []

		numseed = int(seed)

		currentInfo = numseed

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

		allSeedsInfo.append(seedInfo)

	lowest = 0

	for info in allSeedsInfo:
		if lowest == 0:
			lowest = info[7]
		elif info[7] < lowest:
			lowest = info[7]

	print(lowest)

def main():
    solution5()  

if __name__ == "__main__":
    main()