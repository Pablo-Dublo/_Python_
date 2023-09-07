print("Przekształcimy liczbę na słowa!")
print("Wpisz x by zamknąć program.")
while(True):
    liczba = input("\nPodaj liczbę:")
    slownik = {
        "0":"zero",
        "1":"jeden",
        "2":"dwa",
        "3":"trzy",
        "4":"cztery",
        "5":"pieć",
        "6":"sześć",
        "7":"siedem",
        "8":"osiem",
        "9":"dziewięć",
        "x":"Koniec"}

    ileZnakow = len(liczba)
    for i in range(ileZnakow):
        cyfra = liczba[i]
        print(slownik[cyfra], end=" ")
    if liczba == "x":
        print("Zakonczono program.")
        break