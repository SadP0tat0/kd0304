import random


# 4. Masyvai
# Dirbtinių intelektų uždavinių sprendimui nenaudoti. Googlinkite, arba klauskite.
#
# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
# masyvas = [random.randint(5,25) for i in range(30)]
# print(masyvas)

# arba====================================
masyvas = []
for i in range(30):
    rnum = random.randint(5,25)
    masyvas.append(rnum)
print(masyvas)


# Naudodamiesi 1 uždavinio masyvu:
# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;

kiekis = 0
for x in masyvas:
    if x > 10:
        kiekis += 1
print('Didesni uz 10: ',kiekis)

# Raskite didžiausią masyvo reikšmę;
# max = max(masyvas)
Max = 0
for i in masyvas:
    if i > Max: # loopina if 1st number bigger than 0, 2nd number bigger than 1st etc
        Max = i
print(Max)

# Suskaičiuokite visų reikšmių sumą;
print(sum(masyvas))
pinigine = 0
for i in masyvas:
    if i in masyvas:
        pinigine += i
print(pinigine)

# Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;
supermasyvas = []
for i in range(len(masyvas)):
    supermasyvas.append(masyvas[i] - i)
print('masyvas:', masyvas)
print('supermasyvas', supermasyvas)


# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
masyvas2 = [random.randint(5, 25) for i in range(10)]
for num in masyvas2:
    masyvas.append(num)
print(f'masyvas2, {masyvas2}')
print('masyvas', masyvas)

# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;
porinis = []
neporinis = []
# for i in masyvas:
#     if i % 2 == 0:
#         porinis.append(i)
#     elif i % 2 != 0:
#         neporinis.append(i)
# print('porinis', porinis)
# print('neporinis', neporinis)

for i, num in enumerate(masyvas):
    # print('i', i, 'num', num)
    if i % 2 == 0:
        porinis.append(num)
        # print(f'i: {i}, num: {num}')
        print(porinis)
    if i % 2 != 0:
        neporinis.append(num)
        # print(f'i: {i}, num: {num}')
        print(neporinis)
# Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;
print('------------2g-------------')
neaiskus = []
for i, num in enumerate(masyvas):
    if i % 2 == 0:
        if masyvas[i] > 15:
            masyvas[i] = 0
    neaiskus.append((i, masyvas[i]))
print(neaiskus)
print("Indeksai:", end=' ')
for i, num in neaiskus:
    print(i, end=' ')
print("\nSkaiciai:", end=' ')
for i, num in neaiskus:
    print(num, end=' ')

print()
# for i in range(0, len(masyvas), 2):
#     if masyvas[i] > 15:
#         masyvas[i] = 0
# print(f'pakeistos reiksmes: ', masyvas)

# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
print('-----2h------')

pirmas_maziausias = []
for i, num in enumerate(masyvas):
    if num > 10:
        pirmas_maziausias = i
        break
print("Pirmas maziausais:", pirmas_maziausias)

# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.
print('--------3--------')
raidynas = []
sk = []
for i in range(200):
    sk.append(random.randint(0,3))
r2s = {0:'A', 1:'B', 2:'C', 3:'D'}
for num in sk:
    raidynas.append(r2s[num])
print(raidynas)
# A = raidynas.count('A')
# B = raidynas.count('B')
# C = raidynas.count('C')
# D = raidynas.count('D')
#
# print('A:', A, 'B:', B, 'C:', C, 'D:', D)
A = 0
B = 0
C = 0
D = 0
for letter in raidynas:
    if letter == 'A':
        A += 1
    if letter == 'B':
        B += 1
    if letter == 'C':
        C += 1
    if letter == 'D':
         D += 1

print(f"A: {A}, B: {B}, C: {C}, D: {D}")

# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.
print('-----------------4--------------------')

raidynas.sort()
print(raidynas)


# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes. Paskaičiuokite kiek unikalių reikšmių kombinacijų gavote.
print('-----------5------------')
rand1 = [random.choice(['A', 'B', 'C', 'D']) for _ in range(200)]
rand2 = [random.choice(['A', 'B', 'C', 'D']) for _ in range(200)]
rand3 = [random.choice(['A', 'B', 'C', 'D']) for _ in range(200)]
#
# print("rand1:", rand1)
# print("rand2:", rand2)
# print("rand3:", rand3)

combo = [f"{rand1[i]},{rand2[i]},{rand3[i]}" for i in range(200)]
print("combo:", combo)
unicomb = []
for c in combo:
    if c not in unicomb:
        unicomb.append(c)
unikalios = len(unicomb)

print(f"Unikalios reiksmes': {unikalios}")

# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999. Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).
print('-------6------')
koma = []
for _ in range(100):
    while True:
        num = random.randint(100, 999)
        if num not in koma:
            koma.append(num)
            break

print(koma)
koma2 = []
for _ in range(100):
    while True:
        num = random.randint(100, 999)
        if num not in koma2:
            koma2.append(num)
            break

print(koma2)
# Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve, bet nėra antrame 6 uždavinio masyve.
print('-------7-------')

koma3 = []
for num in koma:
    found = False
    for num2 in koma2:
        if num == num2:
            found = True
            break
    if not found:
        koma3.append(num)

print(koma3)

# Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.
print('-------8-------')
koma4 = []
for num in koma:
    for num2 in koma2:
        if num == num2:
            koma4.append(num)
            break

print(koma4)

# Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25. Trečias, pirmo ir antro suma. Ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma ir t.t.
print('-------------9---------------')

Fibonacci = [random.randint(5, 25), random.randint(5, 25)]

# Use a loop to generate the remaining numbers in the array
for i in range(2, 10):
    next = Fibonacci[i-1] + Fibonacci[i-2]
    Fibonacci.append(next)
print(Fibonacci)



