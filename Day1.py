from re import RegexFlag

filename = "input1.txt"

def solution1():

    values = []

    with open(filename) as f:
        content = f.readlines()

    i = 0

    for i in range(len(content)):
        numbers = []
        
        for j in range(len(content[i])):
            if content[i][j].isdigit():
                numbers.append(content[i][j])
            else:
                try:
                    if content[i][j] == "o" and content[i][j + 1] == "n" and content[i][j + 2] == "e":
                        numbers.append("1")
                    elif content[i][j] == "t" and content[i][j + 1] == "w" and content[i][j + 2] == "o":
                        numbers.append("2")
                    elif content[i][j] == "t" and content[i][j + 1] == "h" and content[i][j + 2] == "r" and content[i][j + 3] == "e" and content[i][j + 4] == "e":
                        numbers.append("3")
                    elif content[i][j] == "f" and content[i][j + 1] == "o" and content[i][j + 2] == "u" and content[i][j + 3] == "r":
                        numbers.append("4")
                    elif content[i][j] == "f" and content[i][j + 1] == "i" and content[i][j + 2] == "v" and content[i][j + 3] == "e":
                        numbers.append("5")
                    elif content[i][j] == "s" and content[i][j + 1] == "i" and content[i][j + 2] == "x":
                        numbers.append("6")
                    elif content[i][j] == "s" and content[i][j + 1] == "e" and content[i][j + 2] == "v" and content[i][j + 3] == "e" and content[i][j + 4] == "n":
                        numbers.append("7")
                    elif content[i][j] == "e" and content[i][j + 1] == "i" and content[i][j + 2] == "g" and content[i][j + 3] == "h" and content[i][j + 4] == "t":
                        numbers.append("8")
                    elif content[i][j] == "n" and content[i][j + 1] == "i" and content[i][j + 2] == "n" and content[i][j + 3] == "e":
                        numbers.append("9")
                except:
                    pass

        values.append(numbers[0] + numbers[-1])

    result = 0

    for value in values:
        result += int(value)

    print(result)
    
def main():
    solution1()  

if __name__ == "__main__":
    main()