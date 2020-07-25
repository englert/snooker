with open('snooker.txt', encoding='latin2') as f:
    fejléc = f.readline()
    lista = [ sor.strip().split(';') for sor in f ]

# 3. ________________________________________________________________________

versenyzők_száma = len(lista)
print(f'3. feladat: A világranglistán {versenyzők_száma} versenyző szerepel')

# 4. ________________________________________________________________________

összes_bevétel = sum ( [ int(sor[3]) for sor in lista ] )
átlag = összes_bevétel / versenyzők_száma
print(f'4. feladat: A versenyzők átlagosan {átlag:.2f} fontot kerestek')

# 5. ________________________________________________________________________

kínaiak = [ (int(sor[3]), sor) for sor in lista if sor[2] =='Kína']
helyezés, név, ország, ny = max(kínaiak)[1]
nyeremény = int(ny) * 380
print(f'''5. feladat: A legjobban kereső kínai versenyző:
                  Helyezés: {helyezés}
                  Név: {név}
                  Ország: {ország}
                  Nyeremény összege: {nyeremény} Ft ''')

# 6. ________________________________________________________________________

norvég = [sor for sor in lista if sor[2] == 'Norvégia']
if len(norvég) > 0:
    print(f'6. feladat: A versenyzők között van norvég versenyző.')
else:
    print(f'6. feladat: A versenyzők között nincs norvég versenyző.')

# 7. ________________________________________________________________________

statisztika = dict()
print(      f'7. feladat: Statisztika')
for sor in lista:
    ország = sor[2]
    statisztika[ország] = statisztika.get(ország, 0) + 1
x = [ print(f'        {ország} - {versenyző} fő') for ország, versenyző in statisztika.items() if versenyző > 4]
