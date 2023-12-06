filename = "input6.txt"

def solution6():
    
	content = open(filename).read().split('\n')

	times = content[0].split(":")
	times = times[1].split(' ')
	times = list(filter(None, times))
	dsts = content[1].split(":")
	dsts = dsts[1].split(' ')
	dsts = list(filter(None, dsts))
     
	winning_ways = 0

	time = ""
	dst = ""

	for i in range(len(dsts)):
		dst += dsts[i]

	for i in range(len(times)):
		time += times[i]
		
	distance = 0
	for j in range(0, int(time)):
		distance = (j * (int(time) - j))

		if distance > int(dst):
			winning_ways += 1
	
	print(winning_ways)

def main():
    solution6() 

if __name__ == "__main__":
    main()