filename = "input4.txt"

def solution4():
     
	with open(filename) as f:
		content = f.readlines()
    
	copies = [1] * len(content)

	sumOfCopies = 0

	for i in range(0, len(content)):
		count = 0

		line = content[i].replace("\n", "")

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
	
		if (i + count > len(content) - 1):
			count = len(content) - (1 + i)

		for j in range(copies[i]):
			for k in range(count, 0, -1):
				copies[i + k] += 1
			

	for num in copies:
		sumOfCopies += num
		print(num)
	
	print(sumOfCopies)

def main():
    solution4()  

if __name__ == "__main__":
    main()