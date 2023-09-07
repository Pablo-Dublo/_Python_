import pickle

class Kontakt:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_telefonu = []

    def __str__(self):
        return f"Imię:{self.imie} Nazwisko:{self.nazwisko} " \
               f"\nTelefony:{', '.join(self.numer_telefonu)}"

class Controller:
    def __init__(self):
        self.kontakty = []

    def dodajKontakt(self, imie, nazwisko):
        self.kontakty.append(Kontakt(imie, nazwisko))
        print("Kontakt został dodany")

    def dodajTelefon(self,nazwisko, telefon):
        for i in self.kontakty:
            if i.nazwisko == nazwisko:
                i.numer_telefonu.append(telefon)

    def pokazKontakty(self):
        if len(self.kontakty) == 0:
            print("Nie ma żadnych kontaktów.")
        else:
            for i, kontakt in enumerate(self.kontakty):
                print(f"Kontakt {i + 1}:")
                print(kontakt)

# W tej metodzie, sprawdzamy, czy lista kontaktów jest pusta i w razie potrzeby wyświetlamy stosowny komunikat.\
# W przeciwnym wypadku, iterujemy przez listę i dla każdego kontaktu wywołujemy jego metodę __str__ aby wyświetlić
# jego informacje.

    def usunKontakt(self, nazwisko):

        for x in self.kontakty:
            if x.nazwisko == nazwisko:
                self.kontakty.remove(x)
                print("*Kontakt został usunięty*")
                break
        else:
            print("*Nie znaleziono kontaktu o podanym nazwisku*")

    def usunTelefon(self, nazwisko, telefon):
        for x in self.kontakty:
            if x.nazwisko == nazwisko:
                x.numer_telefonu.remove(telefon)
                break

    def zapis(self):
        plik = open("86_3b.dat", "wb")
        pickle.dump(self.kontakty, plik)
        plik.close()

class App(Controller):
    def __init__(self):
        super().__init__()
        try:
            plik = open("86_3b.dat", "rb")
            self.kontakty = pickle.load(plik)
            plik.close()
        except:
            plik = open("86_3b.dat", "wb")
            plik.close()
        self.menu()

    def menu(self):
        while (True):
            menu = input("1- Dodaj kontakt, \n2- Pokaz kontakty, \n3- Dodaj telefon, "
                         "\n4- Usun kontakt, \n5- Usun telefon, \n6- Koniec \nCo chcesz zrobić?:")

            if (menu == "1"):
                imie = input("Podaj imie:").capitalize()
                nazwisko = input("Podaj nazwisko:").capitalize()
                self.dodajKontakt(imie, nazwisko)
                self.zapis()

            elif (menu == "2"):
                self.pokazKontakty()

            elif (menu == "3"):
                nazwisko = input("Podaj nazwisko").capitalize()
                telefon = input("Podaj telefon").capitalize()
                self.dodajTelefon(nazwisko, telefon)
                self.zapis()

            elif (menu == "4"):
                nazwisko = input("Podaj nazwisko").capitalize()
                self.usunKontakt(nazwisko)
                self.zapis()

            elif (menu == "5"):
                nazwisko = input("Podaj nazwisko").capitalize()
                telefon = int(input("Podaj telefon"))
                self.usunTelefon(nazwisko, telefon)
                self.zapis()

            elif (menu == "6"):
                self.zapis()

            else:
                print("*Wybrano nieistniejącą opcję menu*")
app = App()