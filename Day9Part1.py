def solution8():

    content = open("input8.txt").read().split('\n')

    final_results = []

    for line in content:
        line_numbers = list(map(int, line.split(" ")))

        result_lists = []
        result_lists.append(line_numbers)

        for result_set in result_lists:
            current_results = []

            i = 0

            while not i + 1 >= len(result_set):

                diff = result_set[i + 1] - result_set[i]
                current_results.append(diff)

                i += 1
            
            result_lists.append(list(current_results))

            only_zeroes = True
            for i in range(0, len(current_results)):
                if (int(current_results[i]) != 0):
                    only_zeroes = False
                    break

            if only_zeroes:
                break

        final_results.append(result_lists)

    for i in range(0, len(final_results) - 1):
        for j in range(len(final_results[i]) - 2, 0, -1):
            # print(final_results[i][j])
            # print(final_results[i][j + 1][-1] + final_results[i][j][-1])
            new_int = final_results[i][j + 1][-1] + final_results[i][j][-1]
            final_results[i][j].append(new_int)

    result = 0
    for i in range(0, len(final_results)):
        print(final_results[i][0][-1])
        result += final_results[i][0][-1]

    print(result)


def main():
    solution8() 

if __name__ == "__main__":
    main()