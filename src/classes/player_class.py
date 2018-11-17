class Player:

    def __init__(self):
        self.__sign = ''

    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, new_sign: str):
        self.__sign = new_sign

