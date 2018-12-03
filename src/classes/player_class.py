class Player:

    def __init__(self):
        self.__sign = 'X'

    @property
    def sign(self) -> str:
        """
        Public access for sign
        :return: String with current player sign
        """
        return self.__sign

    @sign.setter
    def sign(self, new_sign: str):
        """
        Public access for setting new sign for player
        :param new_sign: String with new sign
        :return: NoneType
        """
        self.__sign = new_sign

    def sign_change(self):
        """
        Public method for sign change based of bot sign
        :return: NoneType
        """
        if self.__sign == 'O':
            self.__sign = 'X'
        elif self.__sign == 'X':
            self.__sign = 'O'

