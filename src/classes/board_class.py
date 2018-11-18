class Board:

    def __init__(self):
        self.__board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.__win_combo = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
        self.__index = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    @property
    def board(self) -> list:
        return self.__board

    @property
    def win_combo(self) -> list:
        return self.__win_combo

    def update_board(self, place: int, player: str, game_state: bool) -> bool:
        if game_state:
            if self.__board[place] == ' ':
                self.__board[place] = player
                return True
            else:
                return False

    def check_win(self, player) -> bool:
        for x, y, z in self.__win_combo:
            if self.__board[x] == self.__board[y] == self.__board[z] == player:
                return True

    def tie(self) -> bool:
        filled = []
        for i, j in enumerate(self.__board):
            if self.__board[i] != ' ':
                filled.append(i)
        if len(filled) == 9:
            return True
