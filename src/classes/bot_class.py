import random


class Bot:

    def __init__(self, win_combo: list):
        """
        Init method for setting up bot class
        :param win_combo: list of fields combinations for win
        """
        self.__sign = ''
        self.__win_combo = win_combo
        self.__difficulty = 0
        self.__difficulty_dict = {0: 0.45, 1: 0.65, 2: 0.8, 3: 0.95, 4: 1}
        self.__difficulty_lang = {0: 'Easy', 1: 'Medium', 2: 'Hard', 3: 'Expert', 4: 'Unbeatable'}

    @property
    def difficulty(self) -> int:
        """
        Public access to self.__difficulty of the bot
        :return: current bot difficulty
        """
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, lvl: int):
        """
        Public access to set a new difficulty lvl
        :param lvl: new level of difficulty
        :return: NoneType
        """
        if lvl > 4:
            self.__difficulty = 4
        elif lvl < 0:
            self.__difficulty = 0
        else:
            self.__difficulty = lvl

    @property
    def difficulty_lang(self) -> dict:
        """
        Public access to difficulty language dictionary
        :return: Difficulty dictionary
        """
        return self.__difficulty_lang

    def difficulty_up(self):
        """
        Public method for changing difficulty of the bot by 1 up
        :return: NoneType
        """
        self.__difficulty += 1
        if self.__difficulty > 4:
            self.__difficulty = 0

    @property
    def sign(self) -> str:
        """
        Public access to bot sign
        :return: Bot sign
        """
        return self.__sign
    
    @sign.setter
    def sign(self, new_sign: str):
        """
        Public access to setting new bot sign
        :param new_sign: New bot sign
        :return: NoneType
        """
        self.__sign = new_sign

    @staticmethod
    def __get_board_copy(board: list) -> list:
        """
        Private method for copying current board for testing purposes
        :param board: list with board fields values
        :return: Copy of the board
        """
        board_copy = []
        for i in board:
            board_copy.append(i)
        return board_copy

    def __test_win_move(self, board: list, sign, place) -> bool:
        """
        Private method for testing win moves
        :param board: board to test win move
        :param sign: sign to test with
        :param place: place to execute test
        :return: bool with test score
        """
        board_copy = self.__get_board_copy(board)
        board_copy[place] = sign
        return self.__check_win(board_copy, sign)

    def __check_win(self, board: list, player: str) -> bool:
        """
        Private method for checking win
        :param board: list of board fields values
        :param player: sign to test
        :return: True or False depending of the win state for specified sign
        """
        for x, y, z in self.__win_combo:
            if board[x] == board[y] == board[z] == player:
                return True

    @staticmethod
    def __check_tie(board: list) -> bool:
        """
        Private method for checking tie
        :param board: list of board fields values
        :return: True of False depending if there is an empty field left
        """
        return ' ' not in board

    def __test_fork_move(self, board: list, sign: str, place: int) -> bool:
        """
        Private method for testing fork possibilities for given sign and place to test
        :param board: list of board fields values
        :param sign: sign to test
        :param place: place to test
        :return: True or False depending of the existence of fork opportunity
        """
        board_copy = self.__get_board_copy(board)
        board_copy[place] = sign
        winning_moves = 0
        for i in range(9):
            if self.__test_win_move(board_copy, sign, i) and board_copy[i] == ' ':
                winning_moves += 1
        return winning_moves >= 2
        
    def move(self, board: list, player_sign: str) -> int:
        """
        Public method for bot to apply strategy for picking next move
        :param board: list of board fields values
        :param player_sign: opponent sign
        :return: place to strike for bot
        """
        # mistake_chance = random.random()
        max_chance = self.__difficulty_dict[self.__difficulty]
        # if 0 <= mistake_chance <= max_chance:

        # check for bot win possibility
        mistake_chance = random.random()
        if 0 <= mistake_chance <= max_chance:
            for i in range(9):
                if board[i] == ' ' and self.__test_win_move(board, self.__sign, i):
                    return i

        # check for player win possibility
        mistake_chance = random.random()
        if 0 <= mistake_chance <= max_chance:
            for i in range(9):
                if board[i] == ' ' and self.__test_win_move(board, player_sign, i):
                    return i

        # check bot fork opportunities
        mistake_chance = random.random()
        if 0 <= mistake_chance <= max_chance:
            for i in range(9):
                if board[i] == ' ' and self.__test_fork_move(board, self.__sign, i):
                    return i

        # check player fork opportunities
        mistake_chance = random.random()
        if 0 <= mistake_chance <= max_chance:
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
        mistake_chance = random.random()
        if 0 <= mistake_chance <= max_chance and board[4] == ' ':
                return 4

        # play corner
        mistake_chance = random.random()
        if 0 <= mistake_chance <= max_chance and ' ' in [board[0], board[2], board[6], board[8]]:
            while True:
                random_corner = random.choice([0, 2, 6, 8])
                if board[random_corner] == ' ':
                    return random_corner

        # play side
        mistake_chance = random.random()
        if 0 <= mistake_chance <= max_chance and ' ' in board[1:8:2]:
            while True:
                random_side = random.choice([1, 3, 5, 7])
                if board[random_side] == ' ':
                    return random_side

        while True:
            pick = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            if board[pick] == ' ':
                return pick
