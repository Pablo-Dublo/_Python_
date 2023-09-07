szto = int(input("Wybierz figurę której obliczysz pole i obwód: \n Trójkąt(1), Prostokąt(2), Koło(3) :"))

if(szto==1):
    trojkat = int(input("Czy Twój trójkąt jest równoramienny?: Tak(1) / Nie(2)."))
    if(trojkat==1):
        a = float(input("Podaj długośc podstawy trójkąta:"))
        poleTrojkataR = a * (a**2)
        obwodTrojkRowno = a + a + a
        print(f"Pole trójkąta równoramiennego wynosi {poleTrojkataR}, zaś obwód to {obwodTrojkRowno}.")

    if(trojkat==2):
        h = float(input("Podaj wysokość trójkąta:"))
        a = float(input("Podaj długośc podstawy 'a' trójkąta:"))
        b = float(input("Podaj długośc podstawy 'b' trójkąta:"))
        c = float(input("Podaj długośc podstawy 'c' trójkąta:"))
        poleTrojkata = (1 / 2 * a * h)
        obwodTrojk = a + b + c
        print(f"Pole trójkąta wynosi {poleTrojkata}, zaś obwód to {obwodTrojk}.")

if (szto==2):
    a = float(input("Podaj pierwszy bok prostokąta:"))
    b = float(input("Podaj drugi bok prostokąta:"))
    poleProst = a * b
    obwodProst = 2*(a+b)
    print(f"Pole prostokąta wynosi {poleProst}, zaś obwód prostokąta to {obwodProst}")

if (szto==3):
    r = float(input("Podaj promień koła:"))
    poleKola = 3.14 * (r**2)
    obwodKola = 2 * 3.14 * r
    print(f"Pole koła wynosi {poleKola}, zaś obwód koła to {obwodKola} ")
