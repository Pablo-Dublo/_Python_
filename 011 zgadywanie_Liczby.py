import random

print("Zagramy w zgadywankę! "
      "\nZgadnij jaka liczba została wylosowana przez komputer. "
      "\nPrzedział liczbowy to 1-100 "
      "\n*** Masz 5 żyć. ***")

while(True):
    los = random.randint(1, 100)
    ilosc = 0
    while True:
        print("-----")
        liczba = int(input("Podaj liczbę:"))
        if (liczba > los):
            print("Podałeś za dużą liczbę. Tracisz jedno życie.")
            ilosc +=1
            print(f"Utraciłeś już {ilosc} z 5 żyć!")
        elif (liczba < los):
            print("Podałeś za małą liczbę. Tracisz jedną życie.")
            ilosc +=1
            print(f"Utraciłeś już {ilosc} z 5 żyć!")
        elif (liczba == los):
            koniec = False
            print("Gratulacje")
            break
        if (ilosc == 5):
            print("Przegrałeś!")
            print(f"Liczba wylosowana przez komputer to {los}")
            break
    wybor = input("Czy chcesz zagrać jeszcze raz? T/N ")
    if wybor.upper() == "T":
        continue
    else:
        print("Zakończyłeś proces gry")