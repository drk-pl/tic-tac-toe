class Player:

    def __init__(self):
        self.__sign = 'X'

    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, new_sign: str):
        self.__sign = new_sign

    def sign_change_x(self):
        self.__sign = 'X'

    def sign_change_o(self):
        self.__sign = 'O'
