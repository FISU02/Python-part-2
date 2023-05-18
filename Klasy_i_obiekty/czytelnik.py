class czytelnik:
    id: int = -1

    def __init__(self,
                 imie:str, nazwisko:str, wiek:int):
        
        czytelnik.id+=1

        self.id = czytelnik.id
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek 

    
    def get_id(self):
        return self.id
    def get_imie(self):
        return self.imie
    def get_nazwisko(self):
        return self.nazwisko
    def get_wiek(self):
        return self.id
    





