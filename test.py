dupa = [["eee","rrr"],["fff","ttt"],["eee","eee"]]
unique_dupa =[]

i = 0
while i < len(dupa):
    unique_dupa.append(list(set(dupa[i])))
    i += 1


print(unique_dupa)
print(dupa)


counter = 0
i = 0
while i < len(dupa):
    if dupa[i] != unique_dupa[i]:
        counter += 1
    i += 1

print(counter)