import kalkulator


    


while True:
        kalkulator.menu()
        wybor = input("Wybierz działanie (1-dodawanie, 2-odejmowanie, 3-mnożenie, 4-dzielenie, 5-wyjście): ")

        if wybor == "5":
            break

        if wybor not in ["1", "2", "3", "4"]:
            print("Nieprawidłowy wybór")
            continue

        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        if wybor == "1":
            wynik = kalkulator.dodawanie(a, b)
        elif wybor == "2":
            wynik = kalkulator.odejmowanie(a, b)
        elif wybor == "3":
            wynik = kalkulator.mnozenie(a, b)
        elif wybor == "4":
            if b == 0:
                print("Nie można dzielić przez zero")
                continue
            wynik = kalkulator.dzielenie(a, b)

        print(f"Wynik: {wynik}")


print("Koniec programu")