filename = "input5.txt"

def solution5():
	with open(filename) as f:
		content = f.read()

	splitFile = content.split("\n\n")
      
	seeds = splitFile[0].replace("seeds: ", "").split(" ")

	seedRanges = []

	for i in range(0, len(seeds), 2):
		seedRanges.append(int(seeds[i]))
		seedRanges.append((int(seeds[i]) + int(seeds[i + 1])))
		# print(seedRanges[i])
		# print(seedRanges[i + 1])
      
	maps = []
      
	for i in range(1, len(splitFile)):
		splitMap = splitFile[i].split(":")
		maps.append(splitMap[1])


	c_ranges = [[] for _ in range(0, 8)]
	c_ranges[0] = seedRanges

	locations = []

	ranges = []

	for i in range(0, len(seedRanges), 2):
		ranges.append([seedRanges[i], seedRanges[i + 1]])
		results = []

		for _map in maps:
			while ranges:
				
				min_value, max_value = ranges.pop()

				mapLine = _map.split("\n")
				mapLine = filter(None, mapLine)
				for line in mapLine:
					mapValues = line.split(" ")
					
					#left value
					
					map_range_start = int(mapValues[1])
					map_range_reach = int(mapValues[2])
					trsln = int(mapValues[0]) - map_range_start

					map_range_end = map_range_start + (map_range_reach)

					if map_range_end <= min_value or max_value <= map_range_start:
						continue

					if (min_value < map_range_start):
						new_range_min = min_value
						new_range_max = map_range_start						
						ranges.append([new_range_min, new_range_max])
						min_value = map_range_start
					if (max_value > map_range_end):
						new_range_min = map_range_end
						new_range_max = max_value						
						ranges.append([new_range_min, new_range_max])
						max_value = map_range_end
					results.append([new_range_min + trsln, new_range_max + trsln])
					break
				else:
					results.append([new_range_min + trsln, new_range_max + trsln])
			ranges = results
			results = []
	locations += ranges

	print(min(loc[0] for loc in locations))

def main():
    solution5()  

if __name__ == "__main__":
    main()