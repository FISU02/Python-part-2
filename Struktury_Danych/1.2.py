slowo=input("Podaj wyraz ")
reversedstring=''.join(reversed(slowo))
if slowo == reversedstring:
    print("Palindrom")
else:
    print("słowo nie jest palindromem")
