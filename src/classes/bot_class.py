import random


class Bot:

    def __init__(self, win_combo: list):
        self.__sign = ''
        self.__win_combo = win_combo
        self.__difficulty = 0
        self.__difficulty_dict = {0: 0.5, 1: 0.7, 2: 0.9, 3: 1}

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

    def difficulty_up(self, lvl):
        self.__difficulty = lvl

    @property
    def sign(self) -> str:
        return self.__sign
    
    @sign.setter
    def sign(self, new_sign: str):
        self.__sign = new_sign
        
    def move(self, board: list, player_sign) -> int:
        mistake_chance = random.random()
        max_chance = self.__difficulty_dict[self.__difficulty]
        if 0 <= mistake_chance <= max_chance:
            for x, y, z in self.__win_combo:
                if board[x] == self.__sign and board[y] == self.__sign and board[z] == ' ':
                    return z
                if board[x] == self.__sign and board[z] == self.__sign and board[y] == ' ':
                    return y
                if board[z] == self.__sign and board[y] == self.__sign and board[x] == ' ':
                    return x

            for x, y, z in self.__win_combo:
                if board[x] == player_sign and board[y] == player_sign and board[z] == ' ':
                    return z
                if board[x] == player_sign and board[z] == player_sign and board[y] == ' ':
                    return y
                if board[z] == player_sign and board[y] == player_sign and board[x] == ' ':
                    return x

            if board[0] == board[8] == player_sign or board[2] == board[6] == player_sign:
                return random.choice([1, 3, 5, 7])

            if board[3] == board[7] == player_sign:
                if board[6] == ' ':
                    return 6
            elif board[7] == board[5] == player_sign:
                if board[8] == ' ':
                    return 8
            elif board[5] == board[1] == player_sign:
                if board[2] == ' ':
                    return 2
            elif board[1] == board[3] == player_sign:
                if board[0] == ' ':
                    return 0

            if board[4] == player_sign:
                while True:
                    corners = [0, 2, 6, 8]
                    corners_taken = []
                    for i in corners:
                        if board[i] == self.__sign:
                            corners_taken.append(i)
                    if len(corners_taken) != 0:
                        break
                    else:
                        corner = random.choice([0, 2, 6, 8])
                        if board[corner] == ' ':
                            return corner

            if board[4] == ' ':
                return 4

        while True:
            rest = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            if board[rest] == ' ':
                return rest
