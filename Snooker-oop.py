'''
snooker.txt
Helyezes;Nev;Orszag;Nyeremeny
    0     1    2        3     
52;Akani Sunny;Thaiföld;118500
'''
#========================= 2. feladat ============================================
'''
2. Olvassa be a snooker.txt állomány sorait és tárolja az adatokat egy olyan
összetett adatszerkezetben (pl. vektor, lista stb.), amely használatával a további
feladatok megoldhatók! Ügyeljen arra, hogy az állomány első sora a mezőneveket
tartalmazza!
'''
class Snooker:
    def __init__(self, sor):
        s = sor.strip().split(';')
        self.helyezés  = s[0]
        self.név       = s[1]
        self.ország    = s[2]
        self.nyeremény = int( s[3] )
        
with open('snooker.txt', encoding='latin2') as f:
    fejléc = f.readline().strip().split(';')
    lista = [ Snooker(sor) for sor in f ]

#=======================================================================================
'''
3. Határozza meg és írja ki a képernyőre a minta szerint, hogy hány versenyző szerepel a
világranglistán!
'''
versenyzők_száma = len(lista)
print(f'3. feladat: A világranglistán {versenyzők_száma} versenyző szerepel')

#===================== 4. feladat ======================================================
'''
4. Határozza meg, hogy a ranglistán szereplő versenyzők átlagosan mekkora bevételre
tettek szert az elmúlt időszakban! Az eredményt két tizedesjegyre kerekítve jelenítse
meg a minta szerint!

formázás:
{:<8.2f}
< balra igazítás
8.2 8 szóköz széles, 2 tizedes hely
f lebegőpont

: a formátumleírás kezdetét jelöli
[fill]align igazítás ezek egyike lehet:
< ­ balra igazítás
> ­ jobbra igazítás
= ­ helyek kitöltése a jel és a tizedesek között
„+000123.456” (csak számok)
^ ­ középre igazított
a fill a kitöltő karakter, alapból „0”
default sign (alapbeállítás jel)
+ ­ pozitív és negatív számokhoz egyaránt használható
­ ­ csak negatív számokhoz használt (alap)
space (szóköz) – pozitív számok bevezető szóköze, „­” a
negatívok előtt
Width (szélesség) int – a minimális mezőszélességet alkalmazza
, , ­ ezreseket elválasztó vessző használata
.precision (pontosság)
.int – számoknál a tizedesek maximális száma, sztringnél
maximális szélesség
type (típus) # ­ sztring, alap
Integers (egész szám)
b – bináris
c – unikód karakterek konvertálása nyomtatás előtt
d – decimális integer, alap, ha integert ad át
o – oktális formátum
x – kisbetűs hexadecimális
X – nagybetűs hexadecimális
n – mint a d, ám a nemzeti tizedesjel használatával

floating point (lebegőpontos):
e – exponens, alap pontosság 6 számjegyes
E – nagybetűs kitevő
f – fixpontos, alap 6 számjegy pontosság
F – a „nan”­t és az „inf”­et nagybetűssé konvertálja
g – általános formátumleírás
G – általános formátum, szükség szerinti nagybetűs formában
n – a g nemzetfüggő
% ­ százalék

'''

bevétel_lista = [ sor.nyeremény for sor in lista ] 
átlag = sum(bevétel_lista) / versenyzők_száma
print(f'4. feladat: A versenyzők átlagosan {átlag:.2f} fontot kerestek')

#===================== 5. feladat ========================================================
'''
5. Határozza meg és írja ki a képernyőre a minta szerint a legjobban kereső kínai játékos
adatait! Feltételezheti, hogy legalább egy kínai versenyző volt, és nem alakult ki
holtverseny közöttük. A nyeremény összegét forintban jelenítse meg! Az átszámoláshoz
380 Ft-os angol font árfolyammal dolgozzon!
minta:
5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: 17
        Név: Yan Bingtao
        Ország: Kína
        Nyeremény összege: 108 300 000 Ft
'''

kínaiak = [ ( sor.nyeremény, sor) for sor in lista if sor.ország =='Kína']
nyeremény, adatok = max(kínaiak)
print(f'''
**5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: {adatok.helyezés}
        Név: {adatok.név}
        Ország: {adatok.ország}
        Nyeremény összege: {adatok.nyeremény * 380} Ft
''')

'''
6. Határozza meg, hogy a világranglistán található-e norvég játékos!
6. feladat: A versenyzők között van norvég versenyző.
'''
norvég = [sor for sor in lista if sor.ország == 'Norvégia']
if len(norvég) > 0:
    print(f'6. feladat: A versenyzők között van norvég versenyző.')
else:
    print(f'6. feladat: A versenyzők között nincs norvég versenyző.')
    
'''
7. Készítsen statisztikát országok szerinti csoportosításban a versenyzők számáról! Csak
azok az országok jelenjenek meg a minta szerint, amelyekből több mint négy
versenyző szerepel a világranglistán!
7. feladat: Statisztika
    Kína - 29 fő
    Anglia - 47 fő
    Wales - 10 fő
    Skócia - 6 fő
'''
statisztika = dict()
print(      f'7. feladat: Statisztika')
for sor in lista:
    ország = sor.ország
    statisztika[ország] = statisztika.get(ország, 0) + 1
x = [ print(f'     {ország} - {versenyző} fő') for ország, versenyző in statisztika.items() if versenyző > 4]

