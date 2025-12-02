with open('input.txt', 'r') as file:
    lines = file.readlines()

licznik_przejsc = []
kopia_zmiennej = 50
jedynka = 1
for line in lines:
    char = line[0]
    number = int(line[1:])
    if char == 'R':
        for x in range(number):
            kopia_zmiennej += jedynka
            if kopia_zmiennej == 100: kopia_zmiennej = 0
            licznik_przejsc.append(kopia_zmiennej)
    if char == 'L':
        for x in range(number):
            if kopia_zmiennej == 0: kopia_zmiennej = 100
            kopia_zmiennej -= jedynka
            licznik_przejsc.append(kopia_zmiennej)
print("Licznik przejsc: ",licznik_przejsc)
print("Licznik przejsc: ",licznik_przejsc.count(0))