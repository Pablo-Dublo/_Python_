class Kursant:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Kurs:

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.listaKursantow = []

listaKursow = []

while (True):

    menu = input("1-Dodaj kurs, \n2-Pokaz kursu, \n3-Dodaj kursanta do kursu, \n4-Wypisz kursantow z danego kursu, "
                 "\n5-Usun kurs, \n6-Usun kursanta z kursu, \n7-Koniec \nWybierz numer:")

    if (menu == "1"):
        nazwa = input("Podaj nazwa kursu: ")
        nazwaKursu = Kurs(nazwa)
        listaKursow.append(nazwaKursu)

    elif (menu == "2"):
        for x in listaKursow:
            print(x.nazwa)

    elif (menu == "3"):
        nazwa = input("Podaj nazwa kursu: ")
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")

        for x in listaKursow:
            if (x.nazwa == nazwa):
                osoba = Kursant(imie, nazwisko)
                x.listaKursantow.append(osoba)

    elif (menu == "4"):
        nazwa = input("Podaj nazwa kursu: ")
        for x in listaKursow:
            if (x.nazwa == nazwa):
                for kursant in x.listaKursantow:
                    print(kursant.imie, kursant.nazwisko)

    elif (menu == "5"):
        nazwa1 = input("Podaj nazwa kursu: ")
        for x in listaKursow:
            if (x.nazwa == nazwa1):
                if len(x.listaKursantow) == 0:
                    listaKursow.remove(x)
                    print("Kurs został usunięty")
                else:
                    print("Nie można usunąć kursu, ponieważ jest tam kursant")

    elif (menu == "6"):
        nazwa = input("Podaj nazwa kursu: ")
        nazwisko = input("Podaj nazwisko kursanta: ")
        for x in listaKursow:
            if (x.nazwa == nazwa):
                for kursant in x.listaKursantow:
                    if kursant.nazwisko == nazwisko:
                        x.listaKursantow.remove(kursant)
                        print("Kursant został usunięty z kursu")
                    else:
                        print("Nie znaleziono kursanta o podanym nazwisku na tym kursie")

    elif (menu == "7"):
        break
