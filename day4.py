def get_table_from_file(file_name = "day4text.txt"):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(" ") for element in lines]
    return table


def sort_table(table):
    for passpharse in table:
        i = 0

        while i < len(passpharse):
            passpharse[i] = ''.join(sorted(passpharse[i]))
            i+=1

    return table


def count_elements_with_duplicates(table):
    invalid = 0
    valid = 0

    for passphrase in table:
        unique_passpharse = list(set(passphrase))
        unique_passpharse = sorted(unique_passpharse)
        passphrase = sorted(passphrase)
 
        if unique_passpharse != passphrase:
            invalid += 1
        else:
            valid += 1
 
    print("valid passpharses: " + str(valid))
    print("invalid passpharses: " + str(invalid))
 
def main():
    table = get_table_from_file(file_name = "day4text.txt")
    table = sort_table(table) #comment this line to do not get anagrams into account
    count_elements_with_duplicates(table)
 
 
main()
 
 






