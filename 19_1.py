def zapisz_do_pliku(kod):
    try:
        with open("kody.txt", "a") as f:
            f.write(f"{kod}\n")
    except FileNotFoundError:
        print("Niepoprawny plik")


def dodaj(kod):
    if len(kod) != 6 and kod[2] != '-':
        raise Exception("Zle wczytany kod")
    for i, num in enumerate(kod):
        if i == 2:
            continue
        if not num.isnumeric():
            raise Exception("Zły kod")
    zapisz_do_pliku(kod)


kod = input("Podaj kod pocztowy przykład  XX-XXX: ")
try:
    dodaj(kod)
    print("Dodano kod do pliku")
except Exception as add:
    print(add)
