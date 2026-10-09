# Liftteher – mintamegoldás (javítói kulcs)
# Témák: tárolás listában, bekérés, összegzés, eldöntés, keresés (első találat).
# Alternatív tesztadat: utasok = [50, 60, 70], teherbírás 200
#   -> összes tömeg 180, "Mindenki elfér.", 4. feladat: nincs 100 kg feletti utas.

# 1. feladat: az utasok tömege (kg) listában
utasok = [72, 85, 64, 91, 58, 103, 77, 69, 88, 95, 60, 81]

# 2. feladat: bekérés – a feliratnak a bekérés ELŐTT kell megjelennie (az input() paramétere)
teherbiras = int(input("2. feladat: A lift teherbírása (kg): "))

# 3. feladat: összegzés, majd eldöntés
osszeg = 0
for tomeg in utasok:
    osszeg = osszeg + tomeg
# pontosan a teherbírásnak megfelelő tömeg még elfér, ezért <= a helyes reláció
if osszeg <= teherbiras:
    print(f"3. feladat: Az összes tömeg {osszeg} kg. Mindenki elfér.")
else:
    print(f"3. feladat: Az összes tömeg {osszeg} kg. Nem fér el mindenki.")

# 4. feladat: keresés – az első 100 kg-nál nehezebb utast keressük
talalt_index = -1                    # -1 jelzi, hogy még nem találtunk ilyet
i = 0
while i < len(utasok) and talalt_index == -1:
    if utasok[i] > 100:
        talalt_index = i             # az első találatnál a ciklus feltétele leállítja a keresést
    i = i + 1
if talalt_index != -1:
    # a sorszám 1-től számozott, ezért index + 1
    print(f"4. feladat: Az első 100 kg feletti utas: {talalt_index + 1}. ({utasok[talalt_index]} kg)")
else:
    print("4. feladat: Nincs 100 kg feletti utas.")
