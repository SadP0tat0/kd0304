import random


# 4. Masyvai
# Dirbtinių intelektų uždavinių sprendimui nenaudoti. Googlinkite, arba klauskite.
#
# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
masyvas = [random.randint(5,25) for i in range(30)]
print(masyvas)

# arba====================================
# masyvas = []
# for i in range(0,30):
#     rnum = random.randint(5,25)
#     masyvas.append(rnum)
# print(masyvas)


# Naudodamiesi 1 uždavinio masyvu:
# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;

kiekis = 0
for i in masyvas:
    if i > 10:
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
print('masyvas2', masyvas2)
print('masyvas', masyvas)

# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;


# Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;
# Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.
# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.
# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes. Paskaičiuokite kiek unikalių reikšmių kombinacijų gavote.
# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999. Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).
# Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve, bet nėra antrame 6 uždavinio masyve.
# Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.
# Sugeneruokite masyvą, kurio indeksus sudarytų pirmo 6 uždavinio masyvo reikšmės, o jo reikšmės iš būtų antrojo masyvo.
# Sugeneruokite 10 skaičių masyvą pagal taisyklę: Du pirmi skaičiai- atsitiktiniai nuo 5 iki 25. Trečias, pirmo ir antro suma. Ketvirtas- antro ir trečio suma. Penktas trečio ir ketvirto suma ir t.t.
# Sugeneruokite 101 elemento masyvą su atsitiktiniais skaičiais nuo 0 iki 300. Reikšmes kurios tame masyve yra ne unikalios pergeneruokite iš naujo taip, kad visos reikšmės masyve būtų unikalios. Išrūšiuokite masyvą taip, kad jo didžiausia reikšmė būtų masyvo viduryje, o einant nuo jos link masyvo pradžios ir pabaigos reikšmės mažėtų. Paskaičiuokite pirmos ir antros masyvo dalies sumas (neskaičiuojant vidurinės). Jeigu sumų skirtumas (modulis, absoliutus dydis) yra didesnis nei | 30 | rūšiavimą kartokite. (Kad sumos nesiskirtų viena nuo kitos daugiau nei per 30)
#
