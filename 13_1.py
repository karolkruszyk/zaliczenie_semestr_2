import random
import os


class Samochod:
    def __init__(self, marka, model, przebieg, rodzaj, kolor, moc, wartosc, nr_identyfikacyjny_pojazdu):
        self.marka = marka
        self.model = marka
        self.przebieg = przebieg
        self.rodzaj = rodzaj
        self.kolor = kolor
        self.moc = moc
        self.wartosc = wartosc
        self.nr_identyfikacyjny_pojazdu = nr_identyfikacyjny_pojazdu

    def maksymalna_predkosc(self):
        max_predkosc_proporcja = 1.4
        return f"{self.marka} jedzie najwięcej z prędkością {max_predkosc_proporcja * self.moc} km/h "

    def jedzprosto(self):
        jazda = random.randint(1, 70)
        if jazda < 20:
            return "\nKurde cos znosi na prawo .... pora na mechanika"
        elif jazda < 50:
            return "\nDobra elegancko jedzie prosto !"
        elif jazda < 70:
            return "\nKurde cos znosi na lewo .... pora na mechanika .."

    def Pokaz_przyspieszenie(self):
        speed = 0
        while self.moc * 1.4 > speed:
            speed += 25
            if speed < self.moc * 1.4:
                print("Taka oto przyspiesza", self.model, speed)

    def Wymiana_Odleju_ITP(self):
        dynstans = int(
            input("\nKiedy Ostatnio wymieniałes olej , Podaj w przejechanych km ? "))
        if dynstans >= 10000:
            return f"\tNależy Zrobić przebieg !"
        elif dynstans >= 9000:
            return f"\tMożesz jeszcze jeździć ale zaniedługo bedzię trzeba wymienić !! "
        else:
            return f"\tMożesz jeszcze spokojnie jeźdznić "

    def OtworzSamochod(self):
        if self.nr_identyfikacyjny_pojazdu == None:
            print("Sory niemasz takiej funkcji ;/")
        else:
            podaj_nr = input(
                "\nSprawdzmy czy masz dobry kluczyk lub czy to nie złodziej chce sprawdzić czy samochód jest otwarty : ")
            for i in range(1, 3):
                if podaj_nr == self.nr_identyfikacyjny_pojazdu:
                    print("\tWeryfikacja Powiodła się ")
                    break
                else:
                    if i == 1:
                        print("\tWeryfikacja Nie Powiodła się ")
                        podaj_nr = input(
                            "Masz Ostatnia szanse , jeśli sie nie uda odpala sie alarm ! :")
                    else:
                        print("\tŁiŁuŁiŁuŁiŁu")

    def __str__(self):
        return f"\nTwój samochód to {self.marka} o przebiegu {self.przebieg} w kolorze {self.kolor} no i oczywiście z mocą {self.moc}"


samochod1 = Samochod("Ferrari", "F3", 144000, "Kabriolet",
                     "Czerwony", 270, 60000, "1FASD")
samochod2 = Samochod("Proshe", "G7", 1200, "Sedan",
                     "Fioletowy", 250, 100000, "3FGDS")
samochod3 = Samochod("Skoda", "Fabia", 270000, "Sedan",
                     "Niebieski", 130, 15000, None)
samochod4 = Samochod("Audi", "A3", 165000, "Hatchback",
                     "Jasny Niebieski", 200, 25000, "2QWER")
samochod5 = Samochod("Audi", "RS7", 12000, "Hatchback",
                     "Mocny Czerwony", 370, 500000, "QZDSA")

samochod1.Pokaz_przyspieszenie()
print(samochod1)
print(samochod1.jedzprosto())
samochod1.OtworzSamochod()
print(samochod1.Wymiana_Odleju_ITP())
print(samochod1.maksymalna_predkosc())

print()
print()
os.system("PAUSE")

samochod3.Pokaz_przyspieszenie()
print(samochod3)
print(samochod3.jedzprosto())
samochod3.OtworzSamochod()
print(samochod3.Wymiana_Odleju_ITP())
print(samochod3.maksymalna_predkosc())
