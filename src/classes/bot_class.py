import random


class Bot:

    def __init__(self, win_combo: list):
        self.__sign = ''
        self.__win_combo = win_combo
        self.__difficulty = 0
        self.__difficulty_dict = {0: 0.45, 1: 0.65, 2: 0.8, 3: 1}
        self.__difficulty_lang = {0: 'Easy', 1: 'Medium', 2: 'Hard', 3: 'Expert'}

    @property
    def difficulty(self) -> int:
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, lvl: int):
        if lvl > 3:
            self.__difficulty = 3
        elif lvl < 0:
            self.__difficulty = 0
        else:
            self.__difficulty = lvl

    @property
    def difficulty_lang(self) -> dict:
        return self.__difficulty_lang

    def difficulty_up(self):
        self.__difficulty += 1
        if self.__difficulty > 3:
            self.__difficulty = 0

    @property
    def sign(self) -> str:
        return self.__sign
    
    @sign.setter
    def sign(self, new_sign: str):
        self.__sign = new_sign

    @staticmethod
    def __get_board_copy(board: list) -> list:
        board_copy = []
        for i in board:
            board_copy.append(i)
        return board_copy

    def __test_win_move(self, board: list, sign, place) -> bool:
        board_copy = self.__get_board_copy(board)
        board_copy[place] = sign
        return self.__check_win(board_copy, sign)

    def __check_win(self, board: list, player: str) -> bool:
        for x, y, z in self.__win_combo:
            if board[x] == board[y] == board[z] == player:
                return True

    @staticmethod
    def __check_tie(board: list) -> bool:
        return ' ' not in board

    def __test_fork_move(self, board: list, sign: str, place: int) -> bool:
        board_copy = self.__get_board_copy(board)
        board_copy[place] = sign
        winning_moves = 0
        for i in range(9):
            if self.__test_win_move(board_copy, sign, i) and board_copy[i] == ' ':
                winning_moves += 1
        return winning_moves >= 2
        
    def move(self, board: list, player_sign: str) -> int:
        mistake_chance = random.random()
        max_chance = self.__difficulty_dict[self.__difficulty]
        if 0 <= mistake_chance <= max_chance:

            # check for bot win possibility
            for i in range(9):
                if board[i] == ' ' and self.__test_win_move(board, self.__sign, i):
                    return i

            # check for player win possibility
            for i in range(9):
                if board[i] == ' ' and self.__test_win_move(board, player_sign, i):
                    return i

            # check bot fork opportunities
            for i in range(9):
                if board[i] == ' ' and self.__test_fork_move(board, self.__sign, i):
                    return i

            # check player fork opportunities
            player_forks = 0
            for i in range(9):
                if board[i] == ' ' and self.__test_fork_move(board, player_sign, i):
                    player_forks += 1
                    temp_move = i
            if player_forks == 1:
                return temp_move
            elif player_forks == 2:
                for i in ([1, 3, 5, 7]):
                    if board[i] == ' ':
                        return i

            # play center
            if board[4] == ' ':
                return 4

            # play corner
            for i in [0, 2, 6, 8]:
                if board[i] == ' ':
                    return i

            # play side
            for i in [1, 3, 5, 7]:
                if board[i] == ' ':
                    return i
        else:
            while True:
                pick = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
                if board[pick] == ' ':
                    return pick
