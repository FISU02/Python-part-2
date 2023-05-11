class czytelnik:
    id: int = -1

    def __init__(self,
                 imie:str, nazwisko:str, wiek:int):
        
        czytelnik.id+=1

        self.__id = czytelnik.id
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wiek = wiek 

    
    def get_id(self) -> int:
        return self.__id
    def get_imie(self):
        return self.__imie
    def get_nazwisko(self):
        return self.__nazwisko
    def get_wiek(self)  -> int:
        return self.__wiek

