class Player:

    def __init__(self):
        self.__sign = 'X'

    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, new_sign: str):
        self.__sign = new_sign

    def sign_change(self):
        if self.__sign == 'O':
            self.__sign = 'X'
        elif self.__sign == 'X':
            self.__sign = 'O'

