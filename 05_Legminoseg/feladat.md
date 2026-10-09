# Gyakorlófeladat 5 – Légminőség-mérés

*Nehézség: ★★★★★ (a középszint felső határa) – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Egy mérőállomás a levegő szálló pormennyiségét (PM10, µg/m³) méri **8:00-tól kezdve 30 percenként** (az első mérés 8:00-kor készült, a következő 8:30-kor, és így tovább). A 8 mérési eredményt a `pm10.txt` fájl tartalmazza. A **-1** érték mérőhibát jelent, ezt az értéket a számításoknál nem szabad figyelembe venni.

```
42,55,-1,61,48,-1,70,66
```

Feltételezheti, hogy legalább egy érvényes mérés van, és a mérések száma páros. Írjon programot, amely az alábbi feladatokat oldja meg!

1. Tárolja el a mérési eredményeket egy megfelelő adatszerkezetben a program forráskódjában!
2. Határozza meg és írja ki az érvényes mérések számát és azok átlagát!
3. Határozza meg és írja ki óránként (8 órától, 9 órától, …) az érvényes mérések összegét! Egy órában két mérés van (pl. 8:00 és 8:30).
4. Határozza meg és írja ki a legnagyobb mért értéket és a mérés időpontját! Ha több ilyen érték van, az elsőt adja meg! Az időpont óra:perc alakú legyen (pl. `9:30`).
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `legminoseg.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához:**

```
2. feladat: Érvényes mérések: 6, átlag: 57.0
3. feladat: 8 órától 97, 9 órától 61, 10 órától 48, 11 órától 136
4. feladat: A legnagyobb érték: 70, időpontja: 11:00
```

## Általános tudnivalók

- A program forráskódját **`legminoseg.py`** néven mentse!
- Az adatokat a program forráskódjában, **listában** tárolja. A(z) `pm10.txt` fájl tartalmát a kódba másolhatja, a programnak fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha az adatokat a kódban kicseréljük (más elemszám, más értékek), ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **30 perc**. Összesen **15 pont** szerezhető.

