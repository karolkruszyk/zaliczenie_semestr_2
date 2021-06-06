import sqlite3
import os
conn = sqlite3.connect("ybook.db")

if not os.path.exists("ybook.db"):
    with conn:
        conn.execute("CREATE TABLE KONTAKTY("
                     "id INTEGER NOT NULL,"
                     "name TEXT NOT NULL,"
                     "surname TEXT NOT NULL,"
                     "number INTEGER NOT NULL,"
                     "PRIMARY KEY('id' AUTOINCREMENT));")
        conn.commit()
else:
    with conn:
        conn.execute("CREATE TABLE IF NOT EXISTS KONTAKTY("
                     "id INTEGER NOT NULL,"
                     "name TEXT NOT NULL,"
                     "surname TEXT NOT NULL,"
                     "number INTEGER NOT NULL,"
                     "PRIMARY KEY('id' AUTOINCREMENT));")
        conn.commit()


class YellowBook:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def add_number(self):

        self.name = input("Wpisz imię osoby: ")
        self.surname = input("Wpisz nazwisko osoby: ")
        self.number = input("Wpisz numer osoby: ")
        conn.execute(
            f"INSERT INTO KONTAKTY (name,surname,number) "
            f"VALUES('{self.name}','{self.surname}',{self.number});"
        )
        conn.commit()
        print("Kontakt dodany!")

    def read_number(self):
        cursor = conn.execute("SELECT * FROM KONTAKTY;")
        result = cursor.fetchall()
        for row in result:
            print(row)

    def delete_number(self):
        YellowBook.read_number(self)
        choice = input("Wpisz numer ID osoby do usunięcia: ")
        confirm = input(
            "Czy chcesz usunąć ten kontakt? Operacji nie można cofnąć! [y]Tak, [n]Nie: ")
        if confirm == "y" or confirm.lower == "y":
            conn.execute(f"DELETE FROM KONTAKTY WHERE id='{choice}';")
            conn.commit()
        else:
            print("Usunięcie cofnięte!")

    def update_number(self):
        YellowBook.read_number(self)
        choice = input("Wpisz numer ID osoby do aktualizacji: ")
        self.number = input("Podaj nowy numer tej osoby: ")
        conn.execute(
            f"UPDATE KONTAKTY SET number='{self.number}' WHERE id='{choice}'")
        print("Kontakt zaktualizowany!")
        conn.commit()

    def menu(self):
        while True:
            choice = input("Witaj! Wybierz co chcesz zrobić: \n"
                           "[1]Dodać kontakt,\n"
                           "[2]Wypisać kontakty,\n"
                           "[3]Usunąć kontakt,\n"
                           "[4]Zaktualizować kontakt,\n"
                           "[q]Wyjść: ")

            if choice == "1":
                YellowBook.add_number(self)
            elif choice == "2":
                YellowBook.read_number(self)
            elif choice == "3":
                YellowBook.delete_number(self)
            elif choice == "4":
                YellowBook.update_number(self)
            elif choice == "q" or choice.lower() == "q":
                conn.close()
                break
            else:
                print("Brak takiego wyboru.")


YellowBook.menu(YellowBook)
