# Légminőség-mérés – mintamegoldás (javítói kulcs)
# Témák: tárolás listában, hibás adatok (-1) kiszűrése, csoportosítás indexszel, időpont számítása.
# Alternatív tesztadat: meresek = [10, 20, 30, 40]
#   -> 4 érvényes mérés, átlag 25.0; 8 órától 30, 9 órától 70; legnagyobb: 40, időpontja: 9:30.

# 1. feladat: a mérések 8:00-tól 30 percenként készültek (az első 8:00-kor), -1 = mérőhiba
meresek = [42, 55, -1, 61, 48, -1, 70, 66]

# 2. feladat: szűrt megszámlálás és összegzés – a -1 értékeket nem vesszük figyelembe
darab = 0
osszeg = 0
for meres in meresek:
    if meres != -1:
        darab = darab + 1
        osszeg = osszeg + meres
atlag = osszeg / darab               # a feladat szerint van legalább egy érvényes mérés
print(f"2. feladat: Érvényes mérések: {darab}, átlag: {atlag}")

# 3. feladat: óránkénti összeg – óránként 2 mérés van, az i. óra mérései a 2*i és 2*i+1 indexűek
szoveg = []
for ora in range(len(meresek) // 2):
    ora_osszeg = 0
    for index in (2 * ora, 2 * ora + 1):
        if meresek[index] != -1:     # a hibás mérés nem kerül az összegbe
            ora_osszeg = ora_osszeg + meresek[index]
    szoveg.append(f"{8 + ora} órától {ora_osszeg}")
print("3. feladat: " + ", ".join(szoveg))

# 4. feladat: maximum és az első előfordulás indexe
legnagyobb = meresek[0]
legnagyobb_index = 0
for i in range(1, len(meresek)):
    if meresek[i] > legnagyobb:      # szigorú „nagyobb”: az első maximum marad meg
        legnagyobb = meresek[i]
        legnagyobb_index = i
# az index-edik mérés ideje: 8:00 + index * 30 perc
percek = legnagyobb_index * 30
ora = 8 + percek // 60
perc = percek % 60
print(f"4. feladat: A legnagyobb érték: {legnagyobb}, időpontja: {ora}:{perc:02d}")
