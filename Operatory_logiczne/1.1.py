
wiek=int(input("Wpisz swój wiek: "))

prawko=True if (input("Czy masz prawo jazdy a2? ")) in ("tak") else False
odIluA2=0
if prawko:
    odIluA2=int(input("Jak długo masz A2 ? podaj wiek "))
if wiek >= 24:
    print("możesz przystąpić do egzaminu")
elif wiek>=20 and wiek <24 and prawko == True and odIluA2>=2:
    print("możesz przystąpić do egzaminu")
else:
    print("Nie możesz przystąpić do egzaminu")

