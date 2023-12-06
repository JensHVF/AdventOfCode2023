filename = "input6.txt"

def solution6():
    
	content = open(filename).read().split('\n')

	times = content[0].split(":")
	times = times[1].split(' ')
	times = list(filter(None, times))
	dst = content[1].split(":")
	dst = dst[1].split(' ')
	dst = list(filter(None, dst))
     
	winning_ways = [0]*4

	for i in range(len(times)):
		time = int(times[i])
		
		distance = 0
		for j in range(0, time):
			distance = (j * (time - j))

			if distance > int(dst[i]):
				winning_ways[i] += 1
	
	result = 1
	for time in winning_ways: 
		result *= time

	print(result)

def main():
    solution6() 

if __name__ == "__main__":
    main()