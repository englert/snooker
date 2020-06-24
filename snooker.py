'''
snooker.txt
Helyezes;Nev;Orszag;Nyeremeny
    0     1    2        3     
52;Akani Sunny;Thaiföld;118500
'''
#import web_pdb; web_pdb.set_trace()
'''
2. Olvassa be a snooker.txt állomány sorait és tárolja az adatokat egy olyan
összetett adatszerkezetben (pl. vektor, lista stb.), amely használatával a további
feladatok megoldhatók! Ügyeljen arra, hogy az állomány első sora a mezőneveket
tartalmazza!
'''

f = open('snooker.txt', encoding='latin2')
fejléc = f.readline().strip().split(';')

lista = list()
for sor in f:
    lista.append(sor.strip().split(';'))




'''
3. Határozza meg és írja ki a képernyőre a minta szerint, hogy hány versenyző szerepel a
világranglistán!
'''
versenyzők_száma = len(lista)
print(f'3. feladat: A világranglistán {versenyzők_száma} versenyző szerepel')

'''


4. Határozza meg, hogy a ranglistán szereplő versenyzők átlagosan mekkora bevételre
tettek szert az elmúlt időszakban! Az eredményt két tizedesjegyre kerekítve jelenítse
meg a minta szerint!
'''
összes_bevétel = 0

for sor  in  lista:
    bevétel = int( sor[3] )
    összes_bevétel += bevétel
átlag = összes_bevétel / versenyzők_száma
print(f'4. feladat: A versenyzők átlagosan {átlag:.2f} fontot kerestek')
#--------------------------

összes_bevétel = sum ( [ int(sor[3]) for sor in lista ] )
átlag = összes_bevétel / versenyzők_száma
print(f'*4. feladat: A versenyzők átlagosan {átlag:.2f} fontot kerestek')




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

maxi = 0
index = 0
for i, sor in enumerate(lista):
    sorint = int(sor[0]) 
    if int(sor[3]) > maxi and sor[2] == 'Kína':
        maxi = int(sor[3])
        index = i
helyezés   = lista[index][0]
név        = lista[index][1]
ország     = lista[index][2]
nyeremény  = int(lista[index][3]) * 380
print(f'''
5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: {helyezés}
        Név: {név}
        Ország: {ország}
        Nyeremény összege: {nyeremény} Ft
''')
#--------------------
maxi = 0
for sor in lista:
    sorint = int(sor[0]) 
    if int(sor[3]) > maxi and sor[2] == 'Kína':
        helyezés   = sor[0]
        név        = sor[1]
        ország     = sor[2]
        nyeremény  = int(sor[3]) * 380
        maxi = int(sor[3])

print(f'''
*5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: {helyezés}
        Név: {név}
        Ország: {ország}
        Nyeremény összege: {nyeremény} Ft
''')
#------------------------
kínaiak = [ (int(sor[3]), sor) for sor in lista if sor[2] =='Kína']
helyezés, név, ország, ny = max(kínaiak)[1]
nyeremény = int(ny) * 380
print(f'''
**5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: {helyezés}
        Név: {név}
        Ország: {ország}
        Nyeremény összege: {nyeremény} Ft
''')

'''
6. Határozza meg, hogy a világranglistán található-e norvég játékos!
6. feladat: A versenyzők között van norvég versenyző.
'''
norvég = [sor for sor in lista if sor[2] == 'Norvégia']
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
    ország = sor[2]
    statisztika[ország] = statisztika.get(ország, 0) + 1
x = [ print(f'     {ország} - {versenyző} fő') for ország, versenyző in statisztika.items() if versenyző > 4]

