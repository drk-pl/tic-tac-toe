class Board:

    def __init__(self):
        """
        Class constructor that sets up initial board parameters
        """
        self.__board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.__win_combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
        self.__index = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    @property
    def board(self) -> list:
        """
        Public access to board list
        :return: Board list
        """
        return self.__board

    @property
    def win_combo(self) -> list:
        """
        Public access to win combinations
        :return: List of win combinations
        """
        return self.__win_combo

    def update_board(self, place: int, player: str) -> bool:
        """
        Public method for updating board field
        :param place: Place where to put sign
        :param player: Sign to put
        :return: Did method put sign into place? (if the place is taken, return False)
        """
        if self.__board[place] == ' ':
            self.__board[place] = player
            return True
        else:
            return False

    def check_win(self, player):
        """
        Public method for win checking
        :param player: Sign to check
        :return: Tuple with win in first index and win fields combinations
        """
        for x, y, z in self.__win_combo:
            if self.__board[x] == self.__board[y] == self.__board[z] == player:
                return True, [x, y, z]

    def tie(self) -> bool:
        """
        Public method for tie check
        :return: True or False depending if there is tie
        """
        filled = []
        for i, j in enumerate(self.__board):
            if self.__board[i] != ' ':
                filled.append(i)
        if len(filled) == 9:
            return True

    def reset(self):
        """
        Public method for reset board fields values
        :return: NoneType
        """
        self.__board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
