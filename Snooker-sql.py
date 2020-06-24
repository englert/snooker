'''
snooker.txt
Helyezes;Nev;Orszag;Nyeremeny
    0     1    2        3     
52;Akani Sunny;Thaiföld;118500
'''
#========================= 2. feladat ============================================
'''
2. Olvassa be a snooker.txt állomány sorait és tárolja az adatokat.
'''
import sqlite3
conn = sqlite3.Connection('snooker.db')
c    = conn.cursor()

def sql(sql_parancs, *args):
    c.execute(sql_parancs, *args)
    return c.fetchall()
    
sql('DROP TABLE if EXISTS tb;')

sql(''' CREATE TABLE IF NOT EXISTS tb (
            helyezés INTEGER NOT NULL,
            név TEXT NOT NULL,
            ország TEXT NOT NULL,
            nyeremény INTEGER NOT NULL
        );
''')
conn.commit()


with open('snooker.txt', encoding='latin2') as f:
    fejléc = f.readline().strip().split(';')
    for sor in f:
        helyezés, név, ország, nyeremény = sor.strip().split(';')
        #sql( f'INSERT INTO tb VALUES( {helyezés}, "{név}", "{ország}", {nyeremény} )' )
        sql( f'INSERT INTO tb VALUES( ?,?,?,? )', (helyezés, név, ország, nyeremény ) )
    conn.commit()

#=========================== 3. feladat ===================================================
'''
3. Határozza meg és írja ki a képernyőre a minta szerint, hogy hány versenyző szerepel a
világranglistán!
'''
versenyzők_száma = sql('SELECT COUNT() FROM tb;')[0][0]
print(f'3. feladat: A világranglistán {versenyzők_száma} versenyző szerepel')

#===================== 4. feladat ======================================================
'''
4. Határozza meg, hogy a ranglistán szereplő versenyzők átlagosan mekkora bevételre
tettek szert az elmúlt időszakban! Az eredményt két tizedesjegyre kerekítve jelenítse
meg a minta szerint!
'''
átlag = sql(' SELECT AVG(nyeremény) FROM tb; ')[0][0]
print(f'4. feladat: A versenyzők átlagosan {átlag:.2f} fontot kerestek')

#===================== 5. feladat ========================================================
'''
5. Határozza meg és írja ki a képernyőre a minta szerint a legjobban kereső kínai játékos
adatait! A nyeremény összegét forintban jelenítse meg! Az átszámoláshoz 1 font = 380 Forint.
'''

helyezés, név, ország, nyeremény, *kacat = sql(' SELECT *, MAX(nyeremény) FROM tb WHERE ország LIKE "Kína" ;')[0]

print(f'''
**5. feladat: A legjobban kereső kínai versenyző:
        Helyezés: {helyezés}
        Név: {név}
        Ország: {ország}
        Nyeremény összege: {nyeremény * 380} Ft
''')

#==================== 6. feladat ===================================
'''
6. Határozza meg, hogy a világranglistán található-e norvég játékos!
'''
####### norvég = [sor for sor in lista if sor.ország == 'Norvégia']

norvég = sql(' SELECT * FROM tb WHERE ország LIKE "Norvégia"; ')
if len(norvég) > 0:
    print(f'6. feladat: A versenyzők között van norvég versenyző.')
else:
    print(f'6. feladat: A versenyzők között nincs norvég versenyző.')
    
'''
7. Készítsen statisztikát országok szerinti csoportosításban a versenyzők számáról! Csak
azok az országok jelenjenek meg a minta szerint, amelyekből több mint négy
versenyző szerepel a világranglistán!
'''

statisztika = sql(' SELECT ország, count() FROM tb GROUP BY ország HAVING COUNT() > 4 ORDER BY count() DESC ')
print(      f'7. feladat: Statisztika')
x = [ print(f'     {ország} - {versenyzők_száma} fő') for ország, versenyzők_száma in statisztika]

