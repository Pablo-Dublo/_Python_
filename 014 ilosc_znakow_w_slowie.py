slowo = str(input("Podaj stwierdzenie które ma zostać przeliczone na ilość znaków i spacji:"))

ilosc = len(f"{slowo}")
print(f"Znaki wprowadze: {ilosc}")

spacje = slowo.count(' ')
print(f"Liczba spacji to: {spacje}")

slowoBezSpacji = slowo.replace(" ", "")
ileSpacji = ilosc - len(slowoBezSpacji)
print(f" Drugi sposobem, spacji jest: {ileSpacji}")