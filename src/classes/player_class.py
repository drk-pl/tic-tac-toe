class Player:

    def __init__(self):
        self.__sign = ''

    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, new_sign: str):
        self.__sign = new_sign

    def move(self) -> int:
        while True:
            try:
                place = int(input(f"Gdzie wpisać {self.__sign} [1-9]? ")) - 1
                if place in range(0, 9):
                    break
            except ValueError:
                print("Podaj liczbę")
                continue
        return place
