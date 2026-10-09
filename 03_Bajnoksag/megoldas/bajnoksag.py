# Bajnokság – mintamegoldás (javítói kulcs)
# Témák: szöveg (string) bejárása, megszámlálás, képlet, eldöntés.
# Alternatív tesztadat: GGDG -> Győzelem: 3, döntetlen: 1, vereség: 0; 10 pont; Veretlen maradt.
#                       VVVVV -> 0, 0, 5; 0 pont; Volt vereség.

# 1. feladat: az eredménysor bekérése (a felirat a bekérés előtt jelenik meg)
eredmenyek = input("1. feladat: Eredménysor: ")

# 2. feladat: karakterenkénti bejárás, három számláló
gyozelem = 0
dontetlen = 0
vereseg = 0
for betu in eredmenyek:              # a string karakterei közvetlenül bejárhatók
    if betu == "G":
        gyozelem = gyozelem + 1
    elif betu == "D":
        dontetlen = dontetlen + 1
    elif betu == "V":
        vereseg = vereseg + 1
print(f"2. feladat: Győzelem: {gyozelem}, döntetlen: {dontetlen}, vereség: {vereseg}")

# 3. feladat: pontszám = győzelmenként 3, döntetlenenként 1, vereségenként 0 pont
pont = gyozelem * 3 + dontetlen * 1
print(f"3. feladat: A csapat {pont} pontot szerzett.")

# 4. feladat: eldöntés – akkor veretlen a csapat, ha a vereségek száma 0
if vereseg == 0:
    print("4. feladat: Veretlen maradt.")
else:
    print("4. feladat: Volt vereség.")
