filename = "input5.txt"

def solution5():
	with open(filename) as f:
		content = f.read()

	splitFile = content.split("\n\n")
      
	seeds = splitFile[0].replace("seeds: ", "").split(" ")

	seedRanges = []

	for i in range(0, len(seeds), 2):
		seedRanges.append(int(seeds[i]))
		seedRanges.append((int(seeds[i]) + int(seeds[i + 1]) - 1))
		# print(seedRanges[i])
		# print(seedRanges[i + 1])
      
	maps = []
      
	for i in range(1, len(splitFile)):
		splitMap = splitFile[i].split(":")
		maps.append(splitMap[1])


	c_ranges = [[] for _ in range(0, 8)]
	c_ranges[0] = seedRanges


	for i in range(0, len(maps)):
			
		for j in range(0, len(c_ranges[i]), 2):

			min_value = c_ranges[i][j]
			max_value = c_ranges[i][j + 1]

			mapLine = maps[i].split("\n")
			mapLine = filter(None, mapLine)
			for line in mapLine:
				mapValues = line.split(" ")
				
				#left value
				trsln = int(mapValues[0])
				range_start = int(mapValues[1])
				range_reach = int(mapValues[2])
				range_end = range_start + (range_reach - 1)

				if (max_value < range_start):
					continue
				elif (min_value > range_end):
					continue

				if (min_value < range_start):
					new_range_min = min_value
					new_range_max = range_start - 1
					c_ranges[i + 1].append(new_range_min)
					c_ranges[i + 1].append(new_range_max)
				if (max_value > range_end):
					new_range_min = range_end + 1
					c_ranges[i][j + 1] = range_end
					c_ranges[i + 1].append(new_range_min)
					c_ranges[i + 1].append(new_range_max)


	for item in c_ranges:
		print(item)

def main():
    solution5()  

if __name__ == "__main__":
    main()