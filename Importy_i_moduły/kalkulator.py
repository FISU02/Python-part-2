def dodawanie(a: float, b: float) -> float:
    """Funkcja zwraca sumę dwóch liczb"""
    return a + b

def odejmowanie(a: float, b: float) -> float:
    """Funkcja zwraca różnicę dwóch liczb"""
    return a - b

def mnozenie(a: float, b: float) -> float:
    """Funkcja zwraca iloczyn dwóch liczb"""
    return a * b

def dzielenie(a: float, b: float) -> float:
    """Funkcja zwraca iloraz dwóch liczb"""
    return a / b

def menu() -> None:
    """Funkcja wyświetla dostępne operacje"""
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")