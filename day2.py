def get_table_from_file(): 
    with open("day2text.txt", "r") as file:
        lines = file.readlines()
        lines = [line.replace("\n","").split("\t") for line in lines]

    return lines


def change_table_to_integers(table):
    i = 0

    while i < len(table):
        x = 0

        while x < len(table[i]):
            table[i][x] = int(table[i][x])
            x += 1
        i += 1

    return table


def count_differences_in_table(table):
    differences_sum = 0
    i = 0

    while i < len(table):
        minimum = min(table[i]) 
        maximum = max(table[i])
        difference = maximum - minimum
        differences_sum += difference  
        i += 1
    
    return differences_sum


def count_division_sum_in_table(table):
    division_sum = 0
    i = 0

    while i < len(table):
        x = 0

        while x < len(table[i]) - 1:
            dividend = table[i][x]

            for divider in table[i]:
                if divider != dividend:
                    if dividend % divider == 0:
                        division_result = dividend / divider
                        division_sum += division_result
            x += 1
            
        i += 1

    return division_sum

def main():
    table = get_table_from_file()
    table = change_table_to_integers(table)
    differences_sum = count_differences_in_table(table)
    division_sum = count_division_sum_in_table(table)
    print("differences sum: " + str(differences_sum))
    print("division sum: " + str(division_sum))

main()

