class Beer:
    def __init__(self, name, voltage, price, rating, comment):
        self.name = name
        self.voltage = voltage
        self.price = price
        self.rating = rating
        self.comment = comment

class Sklep(Beer):
    def __init__(self, list_of_beers):
        self.list_of_beers = list_of_beers
    def sort_by_name(self):
        print("Sortowanie po nazwie:")
        name_list = []
        for beer in list_of_beers:
            name_list.append(beer.name)

        name_list.sort()

        for name in name_list:
            for beer in list_of_beers:
                if beer.name == name:
                    print("nazwa:",beer.name, "%:", beer.voltage, "cena:", beer.price, "zł", "ocena:",beer.rating, "opinia:", beer.comment)
    def sort_by_rating(self):
        print("Sortowanie po ocenie:")
        rating_list = []
        for beer in list_of_beers:
            rating_list.append(beer.rating)
        
        rating_list.sort(reverse=True)

        for rating in rating_list:
            for beer in list_of_beers:
                if beer.rating == rating:
                    print("nazwa:",beer.name, "%:", beer.voltage, "cena:", beer.price, "zł", "ocena:",beer.rating, "opinia:", beer.comment)

b1 = Beer("Lech", 5, 3.5, 2, "Meh")
b2 = Beer("Perła", 6, 3, 10,"Mmm")
b3 = Beer("Dębowe", 9, 2, 5, "Mocne")
list_of_beers = [b1, b2, b3]

s1 = Sklep(list_of_beers)
s1.sort_by_name()
s1.sort_by_rating()