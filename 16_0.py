import sqlite3
con = sqlite3.connect('16_0_baza.db')
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.executescript("""
DROP TABLE IF EXISTS szkolenia;
CREATE TABLE IF NOT EXISTS szkolenia (
id INTEGER PRIMARY KEY ASC,
temat varchar(250) NOT NULL,
kategorie varchar(250) NOT NULL
)""")
cur.executescript("""
DROP TABLE IF EXISTS prowadzacy;
CREATE TABLE IF NOT EXISTS prowadzacy (
id INTEGER PRIMARY KEY ASC,
imie varchar(250) NOT NULL,
nazwisko varchar(250) NOT NULL,
szkolenia_id INTEGER NOT NULL,
FOREIGN KEY(szkolenia_id) REFERENCES
szkolenia(id)
)""")
cur.executescript("""
DROP TABLE IF EXISTS kursanci;
CREATE TABLE IF NOT EXISTS kursanci (
id INTEGER PRIMARY KEY ASC,
imie varchar(250) NOT NULL,
nazwisko varchar(250) NOT NULL,
szkolenia_id
INTEGER NOT NULL,
FOREIGN KEY(szkolenia_id) REFERENCES szkolenia(id)
)""")
cur.execute('INSERT INTO szkolenia VALUES(NULL, ?, ?);',
            ('programowanie', 'informatyka'))
cur.execute('INSERT INTO szkolenia VALUES(NULL, ?, ?);',
            ('grafika komputerowa', 'informatyka'))
cur.execute('INSERT INTO prowadzacy VALUES(NULL, ?, ?, ?);',
            ('Bogdan', 'Nowak', '1'))
cur.execute('INSERT INTO prowadzacy VALUES(NULL, ?, ?, ?);',
            ('Mirek', 'Kowalski', '2'))
cur.execute('INSERT INTO kursanci VALUES(NULL, ?, ?, ?);',
            ('Jan', 'Szymański', '2'))
cur.execute('INSERT INTO kursanci VALUES(NULL, ?, ?, ?) ;',
            ('Michal', 'Woźniak', '1'))
con.commit()


def czytaj_dane():

    with con:
        cur.execute('SELECT * FROM szkolenia')
        wynik_szkolenia = cur.fetchall()
        cur.fetchall()
        print('\nSzkolenia: ')
    for x in wynik_szkolenia:
        print(x['id'], x['temat'], x['kategorie'])
        cur.execute(
            'SELECT * FROM prowadzacy, szkolenia WHERE prowadzacy.szkolenia_id=szkolenia.id')


wynik_prowadzacy = cur.fetchall()
print('\nProwadzacy: ')
for x in wynik_prowadzacy:
    print(x['id'], x['imie'], x['nazwisko'], x['temat'])
cur.execute(
    'SELECT * FROM kursanci, szkolenia WHERE kursanci.szkolenia_id=szkolenia.id')
wynik_kursanci = cur.fetchall()
print('\nKursanci: ')
for x in wynik_kursanci:
    print(x['id'], x['imie'], x['nazwisko'], x['temat'])


def dodaj_kursanta(imie, nazwisko, szkolenie):
    with con:
        cur.execute('INSERT INTO kursanci VALUES(NULL, ?, ?, ?)',
                    (imie, nazwisko, szkolenie))
    print('\nDodano kursanta')


def dodaj_szkolenie(temat, kategoria):

    with con:
        cur.execute('INSERT INTO szkolenia VALUES(NULL, ?, ?)',
                    (temat, kategoria))
        print('\nDodano szkolenie')


def dodaj_prowadzacego(imie, nazwisko, szkolenie):
    with con:
        cur.execute('INSERT INTO prowadzacy VALUES(NULL, ?, ?, ?)',
                    (imie, nazwisko, szkolenie))
        print('\nDodano prowadzacego')


def usun_kursanta(id):
    with con:
        cur.execute('DELETE FROM kursanci WHERE id=?', (id,))
        print('\nUsunieto kursanta')


def usun_prowadzacego(id):
    with con:
        cur.execute('DELETE FROM prowadzacy WHERE id=?', (id,))
        print('\nUsunietoprowadzacego')


def usun_szkolenie(id):
    with con:
        cur.execute('DELETE FROM szkolenia WHERE id=?', (id,))
        print('\nUsunieto szkolenie')


czytaj_dane()
dodaj_kursanta('Bogdan', 'Morawski', '2')
dodaj_szkolenie('gra na gitarze', 'muzyka')
dodaj_prowadzacego('Bonifacy', 'Trebalski', 3)

czytaj_dane()

usun_kursanta(3)
usun_prowadzacego(3)
usun_szkolenie(3)

czytaj_dane()

con.close()
