filename = "input4.txt"

def solution4():
     
	with open(filename) as f:
		content = f.readlines()
    
	sums = [0]*len(content)
	totalSum = 0

	index = 0

	for line in content:
		count = 0
		
		line = line.replace("\n", "")

		splitLine = line.split(":")
		winsAndNums = splitLine[1].split("|")

		wins = winsAndNums[0].split(" ")
		nums = winsAndNums[1].split(" ")

		for win in wins:
			if win != "":
				for num in nums:
					if win == num:
						count += 1
			else:
				continue
	
		for i in range(count):
			if sums[index] == 0:
				sums[index] += 1
			else:
				sums[index] *= 2

		index += 1

	for cardSum in sums:
		totalSum += cardSum
		print(cardSum)

	print(totalSum)

def main():
    solution4()  

if __name__ == "__main__":
    main()