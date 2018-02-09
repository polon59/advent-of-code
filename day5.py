def get_table_from_file(): 
    with open("day5text.txt", "r") as file:
        lines = file.readlines()
        lines = [line.replace("\n","") for line in lines]

    return lines


def change_to_integers(lines):
    for i in range(len(lines)):
        lines[i] = int(lines[i])

    return lines


def counting_operations(lines):
    i = 0
    operations = 0
    while True:
        try:

            if lines[i] >= 3:
                lines[i] -= 1 
                i = i + lines[i] 
                i += 1

            else:             
                lines[i] += 1
                i = i + lines[i] 
                i -= 1

            operations += 1

            if i < 0:
                raise IndexError

        except IndexError:
            print("number of succesful operations: " + str(operations))
            break


def main():
    lines = get_table_from_file()
    lines = change_to_integers(lines)
    counting_operations(lines)


main()