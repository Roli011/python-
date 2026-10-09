# Gyakorlófeladat 4 – Zsebpénz

*Nehézség: ★★★★☆ – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Peti a hét első napján **5000 Ft** zsebpénzt kap. A hét minden napján szeretne vásárolni, a tervezett napi költéseit forintban a `koltes.txt` fájl tartalmazza:

```
1200,800,1500,700,900,1100,400
```

Ha egy napon nincs elég pénze a tervezett vásárlásra (az aznapi költés nagyobb, mint az egyenlege), akkor aznap **nem vásárol**, és a pénze változatlan marad. Ha a költés pontosan egyenlő az egyenleggel, a vásárlás megtörténik.

Írjon programot, amely az alábbi feladatokat oldja meg!

1. Tárolja el a 7 napi tervezett költést egy megfelelő adatszerkezetben a program forráskódjában!
2. Szimulálja a hetet, és írja ki egy sorban, szóközzel elválasztva, mennyi pénze maradt Petinek az egyes napok végén!
3. Határozza meg és írja ki, hány napon maradt el a vásárlás, és melyik volt az első ilyen nap (1-től számozva)! Ha minden vásárlás megtörtént, a „Minden nap sikerült vásárolni.” üzenetet írja ki!
4. Döntse el, hogy a hét végén maradt-e legalább 500 Ft tartaléka! Ha igen, a „Maradt tartalék.”, különben az „Elfogyott a tartalék.” üzenetet írja ki!
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `zsebpenz.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához:**

```
2. feladat: 3800 3000 1500 800 800 800 400
3. feladat: 2 napon maradt el a vásárlás, először az 5. napon.
4. feladat: Elfogyott a tartalék.
```

## Általános tudnivalók

- A program forráskódját **`zsebpenz.py`** néven mentse!
- Az adatokat a program forráskódjában, **listában** tárolja. A(z) `koltes.txt` fájl tartalmát a kódba másolhatja, a programnak fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha az adatokat a kódban kicseréljük (más elemszám, más értékek), ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **30 perc**. Összesen **15 pont** szerezhető.

