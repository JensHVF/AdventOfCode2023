def solution9():

    content = open("input9.txt").read().split('\n')

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

    result = 0
    for i in range(0, len(final_results)):
        for j in range(len(final_results[i]) - 1, 0, -1):
            # print(final_results[i][j])
            # print(final_results[i][j + 1][-1] + final_results[i][j][-1])
            new_int = final_results[i][j - 1][0] - final_results[i][j][0]
            final_results[i][j - 1].insert(0, new_int)

        result += final_results[i][0][0]

    print(result)

def main():
    solution9() 

if __name__ == "__main__":
    main()