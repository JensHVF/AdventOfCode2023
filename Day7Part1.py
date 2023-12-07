def solution7():
	
	content = open("input7.txt").read().split('\n')

	sets = [[] for _ in range(0, 7)] 

	total_winnings = 0

	letter_to_num_dict = {
		"A" : 14,
		"K" : 13,
		"Q" : 12,
		"J" : 11,
		"T" : 10,
		"9" : 9,
		"8" : 8,
		"7" : 7,
		"6" : 6,
		"5" : 5,
		"4" : 4,
		"3" : 3,
		"2" : 2
	}

	for i in range(len(content)):

		splitCard = content[i].split(" ")
		cardStrength = splitCard[0]
		charsCounts = {} 

		for j in range(len(cardStrength)):
			if cardStrength[j] not in charsCounts.keys():
				charsCounts.update({cardStrength[j] : 1})
			else:
				charsCounts[cardStrength[j]] += 1

		for item in charsCounts.items():
			if len(charsCounts) == 1:
				sets[6].append(content[i])
				break
			elif item[1] == 4:
				sets[5].append(content[i])
				break
			elif item[1] == 3:
				if  len(charsCounts.items()) == 2:
					sets[4].append(content[i])
					break
				else:
					sets[3].append(content[i])
					break
			elif item[1] == 2:
				if len(charsCounts.items()) == 3:
					sets[2].append(content[i])
					break
				elif len(charsCounts.items()) == 2:
					sets[4].append(content[i])
					break
				else:
					sets[1].append(content[i])
					break
			elif len(charsCounts) == 5:
				sets[0].append(content[i])
				break

	ordered_list = []

	for i in range(4, -1, -1):
		for j in range(0, len(sets)):
			sets[j].sort(key = lambda x: (letter_to_num_dict[x[i]]))
	
	for i in range(0, len(sets)):
		ordered_list += sets[i]
	

	index = 0
	for item in ordered_list:
		index += 1
		splitItem = item.split(" ")
		# print(index, splitItem[1])
		total_winnings += (int(splitItem[1]) * index)
		

	print(total_winnings)

def main():
	solution7() 

if __name__ == "__main__":
	main()