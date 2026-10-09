# Lépésszámláló – mintamegoldás (javítói kulcs)
# Témák: tárolás listában, összegzés, átlag, maximum-kiválasztás, megszámlálás.
# Alternatív tesztadat a javításhoz: [3000, 15000, 15000, 800]
#   -> összesen 33800, átlag 8450.0, legtöbb 15000 a 2. napon, 2 nap érte el a 10000-et.

# 1. feladat: az adatok eltárolása listában (a lepesek.txt tartalmát a kódba másoltuk)
lepesek = [6500, 8200, 4300, 10100, 7600, 12000, 5400, 9800, 3900, 11200]

# 2. feladat: összegzés – a változó 0-ról indul, minden elemet hozzáadunk
osszeg = 0
for lepes in lepesek:
    osszeg = osszeg + lepes
# az átlaghoz az elemszámot len()-nel kérdezzük le, így más hosszú listával is jó marad
atlag = osszeg / len(lepesek)
print(f"2. feladat: Összesen {osszeg} lépés, átlag: {atlag}")

# 3. feladat: maximum-kiválasztás – az első elemet tekintjük eddigi legnagyobbnak
legtobb = lepesek[0]
legtobb_nap = 1                      # a napokat 1-től számozzuk
for i in range(1, len(lepesek)):
    # szigorú „nagyobb” kell, hogy egyenlőség esetén az ELSŐ maximum maradjon meg
    if lepesek[i] > legtobb:
        legtobb = lepesek[i]
        legtobb_nap = i + 1          # az index 0-tól indul, ezért +1
print(f"3. feladat: A legtöbb lépés: {legtobb}, a {legtobb_nap}. napon.")

# 4. feladat: megszámlálás – a „legalább 10000” feltétel ≥ (és nem >) relációt kér
darab = 0
for lepes in lepesek:
    if lepes >= 10000:
        darab = darab + 1
print(f"4. feladat: {darab} napon volt legalább 10000 lépés.")
