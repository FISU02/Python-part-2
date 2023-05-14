import random

Liczba = random.randint(0,100)

trys= 0

pick=int(input("Zgadnij liczbę "))

while pick != Liczba:
    
    if (pick>Liczba):
        print("Mniej")
        trys += 1
        pick=int(input("Zgadnij liczbę"))
    elif (pick>Liczba):
        print("Mniej")
        trys +=1
        pick=int(input("Zgadnij liczbę"))
    elif():
        print("Udało ci się")
        print("tyle razy próbowałeś zgadnąć: "+trys)
    
    


