sklep = {"sok":2.55, "woda":1.66, "cola":5.55}
koszyk = {}
ile = None

while(True):

    print("\nWitaj w sklepie!\n")
    menu = input("1- Dodaj produkt do koszyka,\n2- Wyswietl zawartosc koszyka, \n3- Kasa/Koniec "
                 "\n4- Usuń przedmiot z koszyka\nCo chcesz zrobić?:")

    if(menu == "1"):
        for x in sklep:
            print(x, sklep[x])

        nazwa = input("Podaj nazwę produktu który chcesz kupić:")
        if nazwa in sklep:
            ile = int(input("Podaj ilość:"))
            koszyk[nazwa] = koszyk.get(nazwa, 0) + ile
            print(koszyk)
        else:
            print("Nie ma takiego produktu")

    elif (menu == "2"):
        for produkt in koszyk:
            print("Produkt:", produkt, "Cena:", sklep[produkt], "Ilość:", koszyk[produkt])

    elif (menu == "3"):
        kwotaKoszyka = 0
        for produkt in koszyk:
            kwotaKoszyka += sklep[produkt]*ile
        print("RAZEM DO ZAPŁATY:", kwotaKoszyka, "PLN")
        break

    elif (menu == "4"):
        nazwa = input("Podaj nazwę produktu który chcesz usunąć z koszyka:")

        if nazwa in koszyk:
            ilosc = int(input(f"Podaj ile chcesz usunąć: {nazwa}:"))

            if ilosc >= koszyk[nazwa]:
                koszyk.pop(nazwa)
                print(f"{nazwa} został usunięty z koszyka.")
            else:
                koszyk[nazwa] -= ilosc
                print(f"{ilosc} sztuk {nazwa} zostało usuniętych z koszyka.")
        else:
                 print("Nie ma takiego produktu w koszyku.")
    else:
        print("Nieprawidłowe polecenie. Wybierz 1, 2, 3 lub 4.")

