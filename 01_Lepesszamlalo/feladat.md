# Gyakorlófeladat 1 – Lépésszámláló

*Nehézség: ★☆☆☆☆ – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Egy okoskarkötő 10 egymást követő nap lépésszámát rögzítette. A napi adatok a `lepesek.txt` fájlban találhatók:

```
6500,8200,4300,10100,7600,12000,5400,9800,3900,11200
```

Írjon programot, amely az alábbi feladatokat oldja meg!

1. Tárolja el a 10 napi lépésszámot egy megfelelő adatszerkezetben a program forráskódjában!
2. Határozza meg és írja ki a lépések összegét és a napi átlagot!
3. Határozza meg és írja ki, hogy mennyi volt a legtöbb lépés, és hányadik napon! Ha több ilyen nap van, az elsőt adja meg! A napokat 1-től számozzuk.
4. Határozza meg és írja ki, hány napon érte el a lépésszám a 10 000-et (a 10 000 is számít)!
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `lepesek.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához:**

```
2. feladat: Összesen 79000 lépés, átlag: 7900.0
3. feladat: A legtöbb lépés: 12000, a 6. napon.
4. feladat: 3 napon volt legalább 10000 lépés.
```

## Általános tudnivalók

- A program forráskódját **`lepesek.py`** néven mentse!
- Az adatokat a program forráskódjában, **listában** tárolja. A(z) `lepesek.txt` fájl tartalmát a kódba másolhatja, a programnak fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha az adatokat a kódban kicseréljük (más elemszám, más értékek), ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **20 perc**. Összesen **15 pont** szerezhető.

