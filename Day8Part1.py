content = open("input8.txt").read().split('\n\n')

instructions = [*content[0]]
mappings = content[1].split("\n")

mappings_dict = {}

for m in mappings:
	splitM = m.split(" = ")
	name = splitM[0]
	directions = splitM[1].replace("(", "").replace(")", "")
	directions = directions.split(", ")
	mappings_dict.update({name : directions})

count_of_times = 0

while current_place != "ZZZ":

	for inst in instructions:

		index_of_direction = 0

		if inst == 'R':
			index_of_direction = 1
		else:
			index_of_direction = 0

		current_place = mappings_dict[current_place][index_of_direction]
		count_of_times += 1

		if (current_place == "ZZZ"):
			break
		
print(count_of_times)
