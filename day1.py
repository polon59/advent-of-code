def get_index_to_compare(listed_number, i):
    index = int(len(listed_number)/2)

    if i < index:
        return index + i
    else: 
        return i - index


def get_number_from_file():
    with open("day1text.txt", "r") as file:
        number = file.readlines()
        number = number[0].replace("\n","")

        return number


def sum_numbers_first_task(listed_number):
    sum_of_numbers1 = 0
    i = 0

    while i < len(listed_number):
        listed_number[i] = int(listed_number[i])
        i +=1

    i = 0

    while i < (len(listed_number) -1) :
        if listed_number[i] == listed_number[i+1]:
            sum_of_numbers1 += listed_number[i]
        i += 1

    if listed_number[0] == listed_number[-1]:
        sum_of_numbers1 += listed_number[-1]
    
    return sum_of_numbers1


def sum_numbers_second_task(listed_number):
    sum_of_numbers2 = 0
    i = 0

    while i < len(listed_number):
        index = get_index_to_compare(listed_number, i)

        if listed_number[i] == listed_number[index]:
            sum_of_numbers2 += listed_number[i]

        i += 1

    return sum_of_numbers2


def main():
    number = get_number_from_file()
    listed_number = list(number)
    sum_of_numbers1 = sum_numbers_first_task(listed_number)
    sum_of_numbers2 = sum_numbers_second_task(listed_number)
    print("task 1 sum: " + str(sum_of_numbers1))
    print("task 2 sum: " + str(sum_of_numbers2))

main()



