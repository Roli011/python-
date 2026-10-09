# Zsebpénz – mintamegoldás (javítói kulcs)
# Témák: tárolás listában, szimuláció szabállyal, megszámlálás, az első előfordulás, eldöntés.
# Alternatív tesztadat: koltes = [100, 100, 100, 100, 100, 100, 100]
#   -> 4900 4800 4700 4600 4500 4400 4300; nem maradt el vásárlás; Maradt tartalék.
#    koltes = [6000, 100, 6000] -> 5000 4900 4900; 2 napon maradt el, először az 1. napon.

# 1. feladat: a tervezett napi költések (Ft) listában
koltes = [1200, 800, 1500, 700, 900, 1100, 400]

# 2. feladat: szimuláció – az egyenleg 5000 Ft-ról indul
egyenleg = 5000
elmaradt = 0                         # az elmaradt vásárlások száma (3. feladathoz)
elso_elmaradt = 0                    # 0: még nem volt elmaradt vásárlás
napi_egyenlegek = []                 # a napi záró egyenlegeket gyűjtjük a kiíráshoz
for i in range(len(koltes)):
    if koltes[i] <= egyenleg:
        egyenleg = egyenleg - koltes[i]   # van elég pénz: vásárol
    else:
        elmaradt = elmaradt + 1           # nincs elég pénz: aznap nem vásárol
        if elso_elmaradt == 0:
            elso_elmaradt = i + 1         # a napokat 1-től számozzuk
    napi_egyenlegek.append(str(egyenleg))
# a lista elemeit szóközzel összefűzve egy sorban írjuk ki
print("2. feladat: " + " ".join(napi_egyenlegek))

# 3. feladat: az elmaradt vásárlások száma és az első ilyen nap
if elmaradt > 0:
    print(f"3. feladat: {elmaradt} napon maradt el a vásárlás, először az {elso_elmaradt}. napon.")
else:
    print("3. feladat: Minden nap sikerült vásárolni.")

# 4. feladat: eldöntés a hét végi egyenlegre – legalább 500 Ft kell
if egyenleg >= 500:
    print("4. feladat: Maradt tartalék.")
else:
    print("4. feladat: Elfogyott a tartalék.")
