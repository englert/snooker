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
# 3. _______________________________________________________________________
versenyzők_száma = len(lista)
print(f'3. feladat: A világranglistán {versenyzők_száma} versenyző szerepel')
# 4. ________________________________________________________________________
bevétel_lista = [ sor.nyeremény for sor in lista ] 
átlag = sum(bevétel_lista) / versenyzők_száma
print(f'4. feladat: A versenyzők átlagosan {átlag:.2f} fontot kerestek')
# 5. _______________________________________________________________________
kínaiak = [ ( sor.nyeremény, sor) for sor in lista if sor.ország =='Kína']
nyeremény, adatok = max(kínaiak)
print(f'''
5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: {adatok.helyezés}
        Név: {adatok.név}
        Ország: {adatok.ország}
        Nyeremény összege: {adatok.nyeremény * 380} Ft
''')
# 6. ________________________________________________________________________
norvég = [sor for sor in lista if sor.ország == 'Norvégia']
if len(norvég) > 0:
    print(f'6. feladat: A versenyzők között van norvég versenyző.')
else:
    print(f'6. feladat: A versenyzők között nincs norvég versenyző.')
#7. __________________________________________________________________________
statisztika = dict()
print(      f'7. feladat: Statisztika')
for sor in lista:
    ország = sor.ország
    statisztika[ország] = statisztika.get(ország, 0) + 1
x = [ print(f'     {ország} - {versenyző} fő') for ország, versenyző in statisztika.items() if versenyző > 4]

