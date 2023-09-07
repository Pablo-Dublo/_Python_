while(True):

    while (True):
        try:
            liczba1 = float(input("Podaj pierwszą liczbę do działania:"))
            break
        except ZeroDivisionError:
            print("Nie dziel przez zero!")
        except ValueError:
            print("Podajemy tylko liczby.")
        except:
            print("Napotkałeś błąd, skontaktuj się z administratorem programu.")

    while (True):
        try:
            liczba2 = float(input("Podaj drugą liczbę:"))
            break
        except ZeroDivisionError:
            print("Nie dziel przez zero!")
        except ValueError:
            print("Podajemy tylko liczby.")
        except:
            print("Napotkałeś błąd, skontaktuj się z administratorem programu.")

    while (True):
        try:
            liczba3 = input("Podaj symbol działania:")
            if (liczba3 == "-"):
                wynik = liczba1 - liczba2
                print(f"Wynik działania {liczba1} - {liczba2} to: {wynik}")
                break
            elif(liczba3 == "+"):
                wynik = liczba1 + liczba2
                print(f"Wynik działania {liczba1} + {liczba2} to: {wynik}")
                break
            elif (liczba3 == "/"):
                wynik = liczba1 / liczba2
                print(f"Wynik działania {liczba1} / {liczba2} to: {wynik}")
                break
            elif (liczba3 == "*"):
                wynik = liczba1 * liczba2
                print(f"Wynik działania {liczba1} * {liczba2} to: {wynik}")
                break
            else:
                print("Podałeś zły symbol.")
        except ZeroDivisionError:
                print("Nie dziel przez zero!")
        except ValueError:
                print("Podajemy tylko liczby.")
        except:
                print("Napotkałeś błąd, skontaktuj się z administratorem programu.")