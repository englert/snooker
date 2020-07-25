
# Snooker világranglista 
## Programozás vizsgafeladat

A snooker játékban különböző szempontok szerint világranglistákat vezetnek. Ebben a
feladatban egy programot kell készítenie, melyben a 2019. 10. 20-án aktuális pénzdíjas
világranglistával kell dolgoznia.

A megoldás során vegye figyelembe a következőket:

1. A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a
képernyőre a feladat sorszámát (például:3. feladat:)!

2. Az egyes feladatokban a kiírásokat a minta szerint készítse el!

3. Az azonosítókat kis- és nagybetűkkel is kezdheti.

4. Az ékezetmentes azonosítók és kiírások is elfogadottak.

5. A program megírásakor az állományban lévő adatok helyes szerkezetét nem kell
ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak
megfelelnek.

6. A megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges bemeneti
adatok mellett is helyes eredményt adjon!

A snooker . txt UTF-8 kódolású forrásállomány soraiban a következő adatokat találja:
```
Helyezes;Nev; Orszag; Nyeremeny
52;Akani Sunny;Thaiföld;118500
7;Allen Mark;Észak-Írország; 681000
72;Anda Zhang;Kína;44750
76;Astley John;Anglia;40000
73;Baird Sam;Anglia;44750
.......
```
Az állomány sorai a versenyzők neve szerinti ábécérendben tárolja a versenyző helyezését a
ranglistán, nevét, országát és az elmúlt időszakban elnyert pénzdíjak összegét angol fontban.
Az állomány első sora az adatok fejlécét tartalmazza. Az adatokat pontosvesszővel
választottuk el.

1. Készítsen konzolalkalmazást (projektet) a következő feladatok megoldásához,
amelynek forráskódját Snooker néven mentse el!

2. Olvassa be a snooker.txt állomány sorait és tárolja az adatokat egy olyan
összetett adatszerkezetben (pl. vektor, lista stb.), amely használatával a további
feladatok megoldhatók! Ügyeljen arra, hogy az állomány első sora a mezőneveket
tartalmazza!

3. Határozza meg és írja ki a képernyőre a minta szerint, hogy hány versenyző szerepel a
világranglistán!

4. Határozza meg, hogy a ranglistán szereplő versenyzők átlagosan mekkora bevételre
tettek szert az elmúlt időszakban! Az eredményt két tizedesjegyre kerekítve jelenítse
meg a minta szerint!

5. Határozza meg és írja ki a képernyőre a minta szerint a legjobban kereső kínai játékos
adatait! Feltételezheti, hogy legalább egy kínai versenyző volt, és nem alakult ki
holtverseny közöttük. A nyeremény összegét forintba jelenítse meg! Az átszámoláshoz
380 Ft-os angol font árfolyammal dolgozzon!

6. Határozza meg, hogy a világranglistán található-e norvég játékos!

7. Készítsen statisztikát országok szerinti csoportosításban a versenyzők számáról! Csak
azok az országok jelenjenek meg a minta szerint, amelyekből több mint négy
versenyző szerepel a világranglistán!

Minta kimenet:
```
3. feladat: A világranglistán 100 versenyző szerepel
4. feladat: A versenyzők átlagosan 183373,50 fontot kerestek
5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: 17
        Név: Yan Bingtao
        Ország: Kína
        Nyeremény összege: 108 300 000 Ft
6. feladat: A versenyzők között van norvég versenyző.
7. feladat: Statisztika
        Kína - 29 fő
        Anglia - 47 fő
        Wales - 10 fő
        Skócia - 6 fő
```
