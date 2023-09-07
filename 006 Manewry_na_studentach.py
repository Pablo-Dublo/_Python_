class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodajOcene(self, ocena):
        self.oceny.append(ocena)

    def wypiszOceny(self):
        for x in self.oceny:
            print(x, end =" ")
        print()

    def policzSrednia(self):
        suma = 0
        for x in self.oceny:
            suma = suma + x
        srednia = suma/len(self.oceny)
        srednia = round(srednia,2)
        return srednia

listaStudentow = []

while(True):

    menu = input("\n1- Dodaj studenta, \n2- Pokaz studentow, \n3- Usun studenta, \n4- Dodaj ocene studentowi, "
                 "\n5- Wypisz oceny studenta, \n6- Wyswietl srednia studenta, \n7- Koniec."
                 "\nCo chcesz zrobić? Wybierz numer:")

    if (menu == "1"):
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        student = Student(imie, nazwisko)
        listaStudentow.append(student)

    elif (menu == "2"):
        for student in listaStudentow:
            print("Imie:", student.imie, "Nazwisko:",student.nazwisko)

    elif (menu == "3"):
        nazwisko = input("Podaj nazwisko: ")
        for student in listaStudentow:
            if student.nazwisko == nazwisko:
                print(f"Usunięto studenta - {nazwisko}")
                listaStudentow.remove(student)
                break

    elif (menu == "4"):
        nazwisko = input("Podaj nazwisko: ")

        for student in listaStudentow:

            if student.nazwisko == nazwisko:
                ocena = int(input("Podaj ocenę: "))
                student.dodajOcene(ocena)
                break

    elif (menu == "5"):
        nazwisko = input("Podaj nazwisko: ")
        for student in listaStudentow:
            if(student.nazwisko == nazwisko):
                student.wypiszOceny()
                break

    elif (menu == "6"):
        nazwisko = input("Podaj nazwisko:")
        for student in listaStudentow:
            if student.nazwisko == nazwisko:
                srednia = student.policzSrednia()
                print("Średnia ocen:", srednia)
                break
            else:
                print("Student nie ma ocen")
                break

    elif (menu == "7"):
        print("Zakończyłeś program.")
        break

    else:
        print("\nWybrałeś nie istniejącą opcję menu.")