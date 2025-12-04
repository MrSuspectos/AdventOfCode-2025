with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()
    przeczytane =[]
    for line in lines:
        temp =[]
        for i in range(len(str(line))):
            if line[i] != '\n':
                temp.append(line[i])
        przeczytane.append(temp)

najwieksze = []
for linia in przeczytane:
    najwieksza = 0
    for i in range(len(linia)):
        for j in range(i, len(linia)):
            if i == j: continue
            liczba = linia[i] + linia[j]
            if int(liczba) > najwieksza: najwieksza = int(liczba)
    najwieksze.append(najwieksza)

# print(najwieksze)
print(sum(najwieksze))