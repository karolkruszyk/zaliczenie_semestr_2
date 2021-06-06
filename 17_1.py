import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

if os.path.exists('17_1.db'):
    os.remove('17_1.db')
# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///17_1.db')  # ':memory:'
# klasa bazowa
BazaModel = declarative_base()


class Film(BazaModel):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    nazwa = Column(String(100), nullable=False)
    rezyser = Column(String(100), default='')
    obsada = Column(String(100), default='')
    dostepne_na = Column(String(100), default='')


# tworzymy tabele
BazaModel.metadata.create_all(baza)
# __tablename__ wskazuje nazwę tabeli w bazie danych, pod którą chcemy przechowywać informacje

# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()
# dodajemy dwie klasy, jeżeli tabela jest pusta


# dodajemy dane wielu uczniów
sesja.add_all([Film(nazwa='Wojna polsko-ruska', rezyser='Jakiś wariat', obsada='Borys Szyc', dostepne_na='Netflix'),
               Film(nazwa='Listy do M', rezyser='Polski wariat',
                    obsada='Tomasz Karolak', dostepne_na='HBO'),
               Film(nazwa='XXX', rezyser='YYY',
                    obsada='ZZZ', dostepne_na='VOD'),
               ])


def czytajdane():
    i = 1
    for film in sesja.query(Film):
        print(i, film.nazwa, film.rezyser, film.obsada, film.dostepne_na)
        i += 1
    print()


def usun_film():
    czytajdane()
    to_delete = input("Jaki film chcesz usunąć: ")
    sesja.delete(sesja.query(Film).get(to_delete))


def edytuj_film():
    czytajdane()
    to_edit = input("Jaki film chcesz zedytować: ")
    inst_film = sesja.query(Film).filter(Film.id == to_edit).one()
    new_name = input("Nowa nazwa: ")
    new_director = input("Nowy reżyser: ")
    new_cast = input("Nowa obsada: ")
    new_vod = input("Nowe VOD: ")
    inst_film.nazwa = sesja.query(Film.nazwa).filter(
        Film.nazwa == new_name).scalar()
    inst_film.rezyser = sesja.query(Film.rezyser).filter(
        Film.rezyser == new_director).scalar()
    inst_film.obsada = sesja.query(Film.obsada).filter(
        Film.obsada == new_cast).scalar()
    inst_film.dostepne_na = sesja.query(Film.dostepne_na).filter(
        Film.dostepne_na == new_vod).scalar()


def menu():
    print("<1> Dodaj film")
    print("<2> Wyświetl filmy")
    print("<3> Edytuj film")
    print("<4> Usuń film")

    while True:
        choice = int(input("Wybierz: "))
        if choice == 1:
            pass
        elif choice == 2:
            czytajdane()
        elif choice == 3:
            edytuj_film()
        elif choice == 4:
            usun_film()


# # zmiana klasy ucznia o id 2
# inst_uczen = sesja.query(Uczen).filter(Uczen.id == 2).one()
# inst_uczen.klasa_id = sesja.query(
#     Klasa.id).filter(Klasa.nazwa == '1B').scalar()


menu()
# zapisanie zmian w bazie i zamknięcie sesji
sesja.commit()
sesja.close()
