with open("input.txt", "r") as file:
    lines = file.readlines()

zmienne = []
for line in lines:
    zmienne.append(line.split(','))

liczby = []
for x in zmienne[0]:
    liczby.append(list(map(int, x.split('-'))))

invalidID = []
for kody in liczby:
    for x in range(kody[0], kody[1]+1):
        polowa = int(len(str(x)) / 2)
        if (len(str(x)) % 2) != 0: continue
        kodString = str(x)
        # print(kodString, "pierwsza polowa ", kodString[:polowa], "druga polowa ", kodString[polowa:])
        if kodString[:polowa] == kodString[polowa:]: invalidID.append(x)

print(sum(invalidID))