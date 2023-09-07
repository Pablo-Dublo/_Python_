from tkinter import *
root = Tk()
root.title("Książka telefoniczna")
root.geometry("700x300")

kontakty = []

class Kontakt:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

def dodajKontakt():
    imie = entry_Imie.get()
    nazwisko = entry_Nazwisko.get()
    telefon = entry_Telefon.get()
    email = entry_Email.get()

    kontakt = Kontakt(imie, nazwisko, telefon, email)
    kontakty.append(kontakt)
    print(kontakty)

    #czyszczenie pól
    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)

    entry_Imie.focus()
    listaKontaktow()

def listaKontaktow():

    listbox_ListaKontaktow.delete(0, END)
    for index, value in enumerate(kontakty):
        listbox_ListaKontaktow.insert(index, f"{value.imie} {value.nazwisko} {value.telefon} {value.email}")

    listbox_ListaKontaktow.select_set(0)

def usunKontakt():
    index = listbox_ListaKontaktow.index(ACTIVE)
    kontakty.pop(index)
    listaKontaktow()

def edytujKontakt():
    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)

    index = listbox_ListaKontaktow.index(ACTIVE)
    entry_Imie.insert(0, kontakty[index].imie)
    entry_Nazwisko.insert(0, kontakty[index].nazwisko)
    entry_Telefon.insert(0, kontakty[index].telefon)
    entry_Email.insert(0, kontakty[index].email)

    button_DodajKontakt.config(text="Zmien kontakt", command=lambda:zmienKontakt(index))

def zmienKontakt(index):
    imie = entry_Imie.get()
    nazwisko = entry_Nazwisko.get()
    telefon = entry_Telefon.get()
    email = entry_Email.get()

    entry_Imie.delete(0, END)
    entry_Nazwisko.delete(0, END)
    entry_Telefon.delete(0, END)
    entry_Email.delete(0, END)

    kontakty[index].imie = imie
    kontakty[index].nazwisko = nazwisko
    kontakty[index].telefon = telefon
    kontakty[index].email = email

    button_DodajKontakt.config(text="Dodaj kontakt", command=dodajKontakt)
    listaKontaktow()

def pokarzSzczegoly():
    index = listbox_ListaKontaktow.index(ACTIVE)
    kontakt = kontakty[index]
    label_ImieSzczegolyValue.config(text=kontakt.imie)
    label_NazwiskoSzczegolyValue.config(text=kontakt.nazwisko)
    label_TelSzczegolyValue.config(text=kontakt.telefon)
    label_EmailSzczegolyValue.config(text=kontakt.email)

lewaRamka = Frame(root)
prawaRamka = Frame(root)
dolnaRamka = Frame(root)
lewaRamka.grid(row=0, column=0, sticky=N, pady=(20,10), padx=20)
prawaRamka.grid(row=0, column=1, sticky=N, pady=20, padx=20)
dolnaRamka.grid(row=1, columnspan=2, sticky=W, pady=5, padx=5)

lebel_ListaKontaktow = Label(lewaRamka, text="Lista kontaktów:")
listbox_ListaKontaktow = Listbox(lewaRamka, width=20, height=7)
button_PokazSzczegoly = Button(lewaRamka, text="Pokaz szczegóły kontaktu", command=pokarzSzczegoly)
button_UsunKontakt = Button(lewaRamka, text="Usun Kontaktu", command=usunKontakt)
button_EdytujKontakt = Button(lewaRamka, text="Edytuj Kontakt", command=edytujKontakt)

lebel_ListaKontaktow.grid(row=0, columnspan=3)
listbox_ListaKontaktow.grid(row=1, columnspan=3)
button_PokazSzczegoly.grid(row=2, column=0)
button_UsunKontakt.grid(row=2, column=1)
button_EdytujKontakt.grid(row=2, column=2)

label_ListaKontaktow = Label(prawaRamka, text="Nowy Kontakt:")
label_Imie = Label(prawaRamka, text="Imię:")
label_Nazwisko = Label(prawaRamka, text="Nazwisko:")
label_Telefon = Label(prawaRamka, text="Telefon:")
label_Email = Label(prawaRamka, text="Email:")
button_DodajKontakt = Button(prawaRamka, text="Dodaj Kontakt", command=dodajKontakt)

label_ListaKontaktow.grid(row=0, columnspan=2)
label_Imie.grid(row=1, column=0, sticky=W)
entry_Imie = Entry(prawaRamka)
entry_Imie.grid(row=1, column=1, sticky=W)

label_Nazwisko.grid(row=2, column=0, sticky=W)
entry_Nazwisko = Entry(prawaRamka)
entry_Nazwisko.grid(row=2, column=1, sticky=W)

label_Telefon.grid(row=3, column=0, sticky=W)
entry_Telefon = Entry(prawaRamka)
entry_Telefon.grid(row=3, column=1, sticky=W)

label_Email.grid(row=4, column=0, sticky=W)
entry_Email = Entry(prawaRamka)
entry_Email.grid(row=4, column=1, sticky=W)

# button_DodajKontakt = Button(prawaRamka, text="Dodaj Kontakt", command=dodajKontakt)
button_DodajKontakt.grid(row=5, columnspan=2, padx=(55,0))
#button_DodajKontakt = Button(prawaRamka, text="Dodaj Kontakt", command=lambda: test2("ALX"))

label_SzczegolyKontaktu = Label(dolnaRamka, text="Szczegóły Kontaktu:")
label_ImieSzczegoly = Label(dolnaRamka, text="Imię:")
label_ImieSzczegolyValue = Label(dolnaRamka, text="...", width=10)
label_NazwiskoSzczegoly = Label(dolnaRamka, text="Nazwisko:")
label_NazwiskoSzczegolyValue = Label(dolnaRamka, text="...", width=10)
label_TelSzczegoly = Label(dolnaRamka, text="Telefon:")
label_TelSzczegolyValue = Label(dolnaRamka, text="...", width=10)
label_EmailSzczegoly = Label(dolnaRamka, text="Email:")
label_EmailSzczegolyValue = Label(dolnaRamka, text="...", width=10)

label_SzczegolyKontaktu.grid(row=0,columnspan=8, sticky=W)
label_ImieSzczegoly.grid(row=1,column=0,)
label_ImieSzczegolyValue.grid(row=1,column=1)
label_NazwiskoSzczegoly.grid(row=1,column=2)
label_NazwiskoSzczegolyValue.grid(row=1,column=3)
label_TelSzczegoly.grid(row=1,column=4)
label_TelSzczegolyValue.grid(row=1,column=5)
label_EmailSzczegoly.grid(row=1,column=6)
label_EmailSzczegolyValue.grid(row=1,column=7)

# przycisk = Button(root, text="Klikaj")
# przycisk.grid(row=0, column=0)

# przycisk2 = Button(root, text="Klikaj2")
# przycisk2.grid(row=0, column=1)

# przycisk3 = Button(root, text="Klikaj3")
# przycisk3.grid(row=1, columnspan=2)


# "Pętla zdarzeń" zamyka kod i nic nie może byc poza tą linijką!
root.mainloop()