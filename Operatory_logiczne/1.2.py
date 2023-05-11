def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Zakończ")

    # Odczytaj wybór użytkownika
    wybor = input("Wybierz operację (1/2/3/4/5): ")

    # Sprawdź wybór użytkownika
    if wybor == '5':
        break
    elif wybor in ('1', '2', '3', '4'):
        
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        
        if wybor == '1':
            print(a, "+", b, "=", dodawanie(a, b))
        elif wybor == '2':
            print(a, "-", b, "=", odejmowanie(a, b))
        elif wybor == '3':
            print(a, "*", b, "=", mnozenie(a, b))
        elif wybor == '4':
            if b == 0:
                print("Nie można dzielić przez zero!")
            else:
                print(a, "/", b, "=", dzielenie(a, b))
    else:
        print("Nieprawidłowy wybór!")

