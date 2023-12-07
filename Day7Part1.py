def solution7():
    
    content = open("input7.txt").read().split('\n')

    line_strengths = [0]*len(content)

    sets = [[]]*7

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

    content.sort(key = lambda x: (letter_to_num_dict[x[0]]))

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
                line_strengths[i] = 7
                sets[6].append(content[i])
                break
            elif item[1] == 4:
                line_strengths[i] = 6
                sets[5].append(content[i])
                break
            elif item[1] == 3:
                if  len(charsCounts.items()) == 2:
                    line_strengths[i] = 5
                    sets[4].append(content[i])
                    break
                else:
                    line_strengths[i] = 4
                    sets[3].append(content[i])
                    break
            elif item[1] == 2:
                if len(charsCounts.items()) == 3:
                    line_strengths[i] = 3
                    sets[2].append(content[i])
                    break
                else:
                    line_strengths[i] = 2
                    sets[1].append(content[i])
                    break
            else:
                line_strengths[i] = 1
                sets[0].append(content[i])
                break

    zippedHands = dict(zip(content, line_strengths))

    ordered_list = []

    for i in range(0, len(sets)):
        sets[i].sort(key = lambda x: (letter_to_num_dict[x[0]]))
        ordered_list += sets[i]
        
    content.sort(key = zippedHands.get)



    #sort by letters according to the order in the dictionary


    # for i in range(0, len(content)):
        
    #     for j in range(0, len(orderedHands)): 
    #         if line_strengths[i] > line_strengths[j]:
    #             orderedHands.insert(j, content[i])
    #             break

    index = 1
    for item in ordered_list:
        splitItem = item.split(" ")
        total_winnings += (int(splitItem[1]) * index)
        print(total_winnings)
        index += 1
        
    print(total_winnings)
        

def main():
    solution7() 

if __name__ == "__main__":
    main()