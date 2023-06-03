import random
play = True
while play == True:
    proba = 1
    liczba = random.randint(0, 100)
    liczba_player = int(input("Twoja liczba: "))
    while liczba_player != liczba:
        if liczba_player > liczba:
            print("liczba jest mniejsza")
        elif liczba_player < liczba:
            print("liczba jest większa")
        liczba_player = int(input("Twoja liczba: "))
        proba+=1
    print(f"Udało się! Zajęło ci to {proba} prób")
    if input("Czy chcesz zagrać jeszcze raz ? wpisz Yes jęsli chcesz ") != "Yes":
        play = False
