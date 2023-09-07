class Pacjent:
    def __init__(self, imie, nazwisko, pesel, adres, kod_Pocztowy, nr_tel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.adres = adres
        self.kod_Pocztowy = kod_Pocztowy
        self.nr_tel = nr_tel
        self.choroby = []

class Przychodnia:
    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.listaPacjentow = []

listaPrzychodni = []

def dodaj_przychodnie():
    nazwaPrzycho = input("Podaj nazwę przychodni:").capitalize()
    miastoPrzycho = input("Podaj miasto przychodni:").capitalize()
    listaPrzychodni.append(Przychodnia(nazwaPrzycho, miastoPrzycho))
    print("*Przychodnia została dodana*")

def usun_przychodnie():
    nazwa = input("Wprowadź nazwę przychodni:").capitalize()
    for przychodnia in listaPrzychodni:
        if przychodnia.nazwa == nazwa:
            if len(przychodnia.listaPacjentow) == 0:
                listaPrzychodni.remove(przychodnia)
                print("*Przychodnia usunięta*")
            else:
                print("*Nie można usunąć przychodni z pacjentami*")

def dodaj_pacjenta_do_przychodni():
    while True:
        nazwa = input("Podaj nazwę przychodni:").capitalize()
        przychodnia_istnieje = False
        for przychodnia in listaPrzychodni:
            if przychodnia.nazwa == nazwa:
                przychodnia_istnieje = True
                break
        if not przychodnia_istnieje:
            print("Podana przychodnia nie istnieje w bazie danych")
            continue
        break

    while True:
        try:
            imie = input("Wprowadź imię pacjenta:").capitalize()
            nazwisko = input("Wprowadź nazwisko pacjenta:").capitalize()
            pesel = int(input("Wprowadź pesel pacjenta:"))
            adres = input("Podaj adres pacjenta:").capitalize()
            kod_pocztowy = int(input("Podaj kod pocztowy pacjenta:"))
            nr_tel = int(input("Podaj numer telefonu pacjenta:"))
            break
        except ValueError:
            print("Wprowadź poprawne dane")

    for przychodnia in listaPrzychodni:
        if przychodnia.nazwa == nazwa:
            pacjent = Pacjent(imie, nazwisko, pesel, adres, kod_pocztowy, nr_tel)
            przychodnia.listaPacjentow.append(pacjent)
            print("Pacjent został dodany")
            break

def edytuj_pacjenta():
    nazwisko = input("Podaj nazwisko pacjenta do edycji:").capitalize()
    for pacjent in listaPrzychodni:
        for p in pacjent.listaPacjentow:
            if p.nazwisko == nazwisko:
                while True:
                    print("Wybierz opcję edycji:")
                    print("1. Imię")
                    print("2. Nazwisko")
                    print("3. PESEL")
                    print("4. Adres")
                    print("5. Kod pocztowy")
                    print("6. Numer telefonu")
                    print("9. Powrót")
                    wybor = int(input("Wybierz opcję: "))
                    if wybor == 1:
                        nowe_imie = input("Podaj nowe imię: ").capitalize()
                        p.imie = nowe_imie
                    elif wybor == 2:
                        nowe_nazwisko = input("Podaj nowe nazwisko: ").capitalize()
                        p.nazwisko = nowe_nazwisko
                    elif wybor == 3:
                        nowy_pesel = int(input("Podaj nowy PESEL: "))
                        p.pesel = nowy_pesel
                    elif wybor == 4:
                        nowy_adres = input("Podaj nowy adres: ").capitalize()
                        p.adres = nowy_adres
                    elif wybor == 5:
                        nowy_kod_pocztowy = int(input("Podaj nowy kod pocztowy: "))
                        p.kod_Pocztowy = nowy_kod_pocztowy
                    elif wybor == 6:
                        nowy_nr_tel = int(input("Podaj nowy numer telefonu: "))
                        p.nr_tel = nowy_nr_tel
                    elif wybor == 9:
                        break
                    else:
                        print("Niepoprawna opcja")
                return
    print("Pacjent o podanym nazwisku nie został znaleziony")

def usun_pacjenta_z_przychodni():
    nazwa = input("Wprowadź nazwę przychodni:").capitalize()
    nazwisko = input("Wprowadź nazwisko pacjenta:").capitalize()
    for przychodnia in listaPrzychodni:
        if przychodnia.nazwa == nazwa:
            for pacjent in przychodnia.listaPacjentow:
                if pacjent.nazwisko == nazwisko:
                    przychodnia.listaPacjentow.remove(pacjent)
                    print("*Pacjent usunięty z przychodni*")

def przenies_pacjenta():
    nazwisko = input("Podaj nazwisko pacjenta:").capitalize()
    nazwa_obecnej = input("Podaj nazwę obecnej przychodni:").capitalize()
    nazwa_nowej = input("Podaj nazwę nowej przychodni:").capitalize()
    for obecna in listaPrzychodni:
        if obecna.nazwa == nazwa_obecnej:
            for pacjent in obecna.listaPacjentow:
                if pacjent.nazwisko == nazwisko:
                    for nowa in listaPrzychodni:
                        if nowa.nazwa == nazwa_nowej:
                            obecna.listaPacjentow.remove(pacjent)
                            nowa.listaPacjentow.append(pacjent)
                            print("*Pacjent został dodany*")

def lista_klinik():
    for klinika in listaPrzychodni:
        print(f"{klinika.nazwa} w {klinika.miasto}")

def lista_pacjentow_w_klinice():
    nazwa = input("Wprowadź nazwę kliniki:").capitalize()
    for klinika in listaPrzychodni:
        if klinika.nazwa == nazwa:
            for pacjent in klinika.listaPacjentow:
                print(f"Dane pacjenta: \nImię:{pacjent.imie} \nNazwisko:{pacjent.nazwisko} \nPesel:{pacjent.pesel}, "
                      f"\nAdres zamieszkania:{pacjent.adres}, "
                      f"\nKod pocztowy: {pacjent.kod_Pocztowy}, \ntel.{pacjent.nr_tel}")

def dodaj_chorobe():
    nazwa = input("Podaj nazwę klinik:").capitalize()
    nazwisko = input("Podaj nazwisko pacjenta:").capitalize()
    for klinika in listaPrzychodni:
        if klinika.nazwa == nazwa:
            for pacjent in klinika.listaPacjentow:
                if pacjent.nazwisko == nazwisko:
                    choroba = input("Podaj chorobę:")
                    pacjent.choroby.append(choroba)
    print("*Dodano chorobę*")

def lista_chorob():
    nazwisko = input("Podaj nazwisko pacjenta:").capitalize()
    for x in listaPrzychodni:
        for pacjent in x.listaPacjentow:
            if pacjent.nazwisko == nazwisko:
                print("Choroby pacjenta:")
                for choroba in pacjent.choroby:
                    print(choroba)

while (True):
        menu = input("\n1- Przychodnia \n2- Pacjent \n3- Koniec \nCo chcesz zrobić?:")

        if (menu == "1"):
            while (True):
                opcje1 = input("\n1- Dodaj przychodnię \n2- Usuń przychodnię \n3- Dodaj pacjenta do przychodni "
                               "\n4- Usuń pacjenta z przychodni \n5- Lista przychodni \n6- Lista pacjentów w przychodni "
                               "\n7- Przenieś pacjenta z placówki do innej placówki \n8- Edytuj dane pacjenta "
                               "\n9- Powrót \nCo chcesz zrobić?:")
                if (opcje1 == "1"):
                    dodaj_przychodnie()
                elif (opcje1 == "2"):
                    usun_przychodnie()
                elif (opcje1 == "3"):
                    dodaj_pacjenta_do_przychodni()
                elif (opcje1 == "4"):
                    usun_pacjenta_z_przychodni()
                elif (opcje1 == "5"):
                    lista_klinik()
                elif (opcje1 == "6"):
                    lista_pacjentow_w_klinice()
                elif (opcje1 == "7"):
                    przenies_pacjenta()
                elif (opcje1 == "8"):
                    edytuj_pacjenta()
                elif (opcje1 == "9"):
                    break
                else:
                    print("*Wybrano złą opcję menu*")
                    continue

        elif (menu == "2"):
            while (True):
                opcja2 = input("\n1- Dodaj chorobę pacjentowi,\n2- Lista chorób pacjenta. "
                               "\n3- Powrót \nCo chcesz zrobić?:")
                if (opcja2 == "1"):
                    dodaj_chorobe()
                elif (opcja2 == "2"):
                    lista_chorob()
                elif (opcja2 == "3"):
                    break
                else:
                    print("*Wybrano złą opcję menu*")
                    continue

        elif (menu == "3"):
            break
        else:
            print("*Wybrano nieistniejącą opcję menu.*")
            continue