class Pracownik:
    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__kontrakt = kontrakt
        self.__pensja = pensja

    def get_imie(self):
        return self.__imie

    def set_imie(self, imie):
        self.__imie = imie

    def get_nazwisko(self):
        return self.__nazwisko

    def set_nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def get_kontrakt(self):
        return self.__kontrakt

    def set_kontrakt(self, kontrakt):
        self.__kontrakt = kontrakt

    def get_pensja(self):
        return self.__pensja

    def set_pensja(self, pensja):
        self.__pensja = pensja

    def wyswietl_wlasciwosci(self):
        return (f"Pracownik {self.__imie} {self.__nazwisko}, "
                f"\nzatrudniony na kontrakcie{self.__kontrakt} otrzyma {self.__pensja}PLN")

class PracownicyController:
    def __init__(self):
        self.pracownicy = []

    def dodajPracownika(self, imie, nazwisko, kontrakt, pensja):
        pracownik = Pracownik(imie, nazwisko, kontrakt, pensja)
        self.pracownicy.append(pracownik)
        print("Pracownik został dodany")

    def pokazPracownikow(self):
        for pracownik in self.pracownicy:
            print(pracownik.wyswietl_wlasciwosci())

    def usunPracownika(self, nazwisko):
        for pracownik in self.pracownicy:
            if pracownik.get_nazwisko() == nazwisko:
                self.pracownicy.remove(pracownik)
                print(f"Pracownik <{nazwisko}> został usunięty.")
                return True
        return False

    def zmienDanePracownikowi(self, nazwisko, nowyKontrakt, pensja):
        for pracownik in self.pracownicy:
            if pracownik.get_nazwisko() == nazwisko:
                pracownik.set_kontrakt(nowyKontrakt)
                pracownik.set_pensja(pensja)
                print("Dane zostały poprawnie zmienione.")
                return True
        return False

class Firma(PracownicyController):
    def __init__(self, nazwaFirmy:str):
        self.nazwaFirmy = nazwaFirmy
        super().__init__()
        self.menu()

    def menu(self):

        while(True):
            print(f"Witaj w firmie {self.nazwaFirmy}")
            print("#### MENU ####")
            dec = input("1-Dodaj, \n2-Pokaz, \n3-Usun, \n4-Zmiana, \n5-Koniec \nCo chcesz zrobić?:")

            if (dec == '1'):
                imie = input("Podaj imię pracownika: ")
                nazwisko = input("Podaj nazwisko pracownika: ")
                kontrakt = input("Podaj kontrakt pracownika: ")
                pensja = input("Podaj pensje pracownika: ")
                self.dodajPracownika(imie, nazwisko, kontrakt, pensja)

            if (dec == '2'):
                self.pokazPracownikow()
            if (dec == '3'):
                nazwisko = input("Podaj nazwisko pracownika: ")
                self.usunPracownika(nazwisko)
            if (dec == '4'):
                nazwisko = input("Podaj nazwisko pracownika: ")
                nowyKontrakt = input("Podaj nowy kontrakt pracownika staz/etat: ")
                pensja = input("Podaj nową pensję pracownika: ")
                self.zmienDanePracownikowi(nazwisko, nowyKontrakt, pensja)
            if (dec == '5'):
                print("Do zobaczenia!")
                break

firma = Firma("Dubland Different Company")