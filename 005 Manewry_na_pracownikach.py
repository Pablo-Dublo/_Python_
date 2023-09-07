
class Pracownik:
    def __init__(self, imie, nazwisko, email, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.telefon = telefon

class PracownikController:

    listaPracownikow = []

    def dodaj(self, imie, nazwisko, email, telefon):
        pracownik = Pracownik(imie, nazwisko, email, telefon)
        self.listaPracownikow.append(pracownik)
        print("Pracownik została pomyślnie dodany!")

    def pokaz(self):
        for pracownik in self.listaPracownikow:
            print(f"Imię: {pracownik.imie} Nazwisko: {pracownik.nazwisko}, "
                  f"Rodzaj kontraktu: {pracownik.email}, Pensja: {pracownik.telefon}")

    def usun(self, nazwisko):
        nazwisko = input("Podaj nazwisko pracownika, którego chcesz usunąć:")
        for i, v in enumerate(self.listaPracownikow):
            if v.nazwisko == nazwisko:
                self.listaPracownikow.pop(i)
                print(f'Pracownik o nazwisku {nazwisko} został usunięty.')
                break
        else:
            print(f'Nie znaleziono pracownika o nazwisku {nazwisko}.')

    def zmien(self, nazwisko, noweImie, noweNazwisko, nowyEmail, nowaTelefon):
        for pracownik in self.listaPracownikow:
            if pracownik.nazwisko == nazwisko:
                pracownik.imie = noweImie
                pracownik.nazwisko = noweNazwisko
                pracownik.email = nowyEmail
                pracownik.telefon = nowaTelefon

    def sprawdzPracownika(self, nazwisko):
        return any(pracownik.nazwisko == nazwisko for pracownik in self.listaPracownikow)

pracownikController = PracownikController()

while (True):

    menu = input("1-Dodaj \n2-Pokaz \n3-Usun \n4-Zmien \n5-Koniec\nCo chcesz zrobić?:")

    if menu == "1":
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        email = input("Podaj email: ")
        telefon = input("Podaj telefon: ")
        pracownikController.dodaj(imie, nazwisko, email, telefon)

    elif menu == "2":
        pracownikController.pokaz()

    elif menu == "3":
        nazwisko = input("Podaj nazwisko do usunięcia Pracownika: ")
        pracownikController.usun(nazwisko)

    elif menu == "4":
        nazwisko = input("Podaj nazwisko Pracownika do zmiany: ")
        noweImie = input("Podaj nowe imie: ")
        noweNazwisko = input("Podaj nowe nazwisko: ")
        nowyEmail = input("Podaj nowy email: ")
        nowaTelefon = input("Podaj nową telefon: ")
        pracownikController.zmien(nazwisko, noweImie, noweNazwisko, nowyEmail, nowaTelefon)

    elif menu == "5":
        print("Zakończyłeś progam.")

    else:
        print("wybrałeś nie istniejącą opcję menu. \nSpróbuj ponownie:")
        continue