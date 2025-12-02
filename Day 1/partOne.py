with open('input.txt', 'r') as file:
    lines = file.readlines()

licznik_zder = 0
zmienna = 50
for line in lines:
    char = line[0]
    number = int(line[1:])
    if char == 'R':
        zmienna += number
        zmienna = zmienna % 100
    if char == 'L':
        zmienna -= number
        zmienna = zmienna % 100
    print(zmienna)
    if zmienna == 0: licznik_zder += 1
print("Licznik zer: ",licznik_zder)