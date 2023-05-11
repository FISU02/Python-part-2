class czytelnik:
    id: int = -1

    def __init__(self,
                 imie:str, nazwisko:str, wiek:int):
        
        czytelnik.id+=1

        self.id = czytelnik.id
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek 

    





