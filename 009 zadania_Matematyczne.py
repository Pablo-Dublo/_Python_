import random

while(True):
    rozwiazanie = 0
    dzialanie = None
    zadanie = None
    poprawnie = 0
    blednie = 0

    for i in range(15):
        los1 = random.randint(1, 10)
        los2 = random.randint(1, 10)
        los3 = random.randint(0, 2)

        if los3 == 0:
            dzialanie = f"{los1} + {los2}"
            wynik = los1 + los2
        elif los3 == 1:
            dzialanie = f"{los1} - {los2}"
            wynik = los1 - los2
        elif los3 == 2:
            dzialanie = f"{los1} * {los2}"
            wynik = los1 * los2

        while True:
            zadanie = int(input(f"Podaj wynik liczb: {dzialanie}="))
            if zadanie == wynik:
                print("Podałeś dobry wynik!")
                rozwiazanie += 1
                poprawnie += 1
                break
            else:
                print("Podałeś zły wynik, spróbuj jeszcze raz.")
                rozwiazanie += 1
                blednie += 1

        if rozwiazanie == 10:
            print(f"Brawo! ukończyłeś 10 zadań! Odpowiedziałeś poprawnie na {poprawnie} pytań, zaś błędnie na {blednie} ")
            break

    graj_jeszcze_raz = input("Czy chcesz zagrać jeszcze raz? (T/N) ")
    if graj_jeszcze_raz.upper() == "N":
        break