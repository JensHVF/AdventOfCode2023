content = open("input8.txt").read().split('\n\n')

instructions = [*content[0]]
mappings = content[1].split("\n")

mappings_dict = {}

from math import gcd

def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // gcd(a, b)
    return a

for m in mappings:
	splitM = m.split(" = ")
	name = splitM[0]
	directions = splitM[1].replace("(", "").replace(")", "")
	directions = directions.split(", ")
	mappings_dict.update({name : directions})


current_places = []
for m in mappings_dict:
	if m[2] == "A":
		current_places.append(m)


count_of_times = 0

found_all = False

dict_of_steps = {}

while not found_all:

	for inst in instructions:

		index_of_direction = 0

		if inst == 'R':
			index_of_direction = 1
		else:
			index_of_direction = 0


		count_of_times += 1
		for i in range(0, len(current_places)):
			current_places[i] = mappings_dict[current_places[i]][index_of_direction]
			if current_places[i][2] == "Z":
				if current_places[i] not in dict_of_steps:
					dict_of_steps.update({current_places[i] : count_of_times})
		
		if len(dict_of_steps) == 6:
			found_all = True
			break

answer = 1
for item in dict_of_steps:
	print(item, " ", dict_of_steps[item])
	answer *= dict_of_steps[item]

print(lcm(*dict_of_steps.values()))


