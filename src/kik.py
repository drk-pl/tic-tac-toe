from src.classes.board_class import Board
from src.classes.player_class import Player
from src.classes.bot_class import Bot
from src.classes.game_class import Game


def main(reset=True):

    def game_loop(state=False):
        game_state = state
        bot_win = False
        move = 0
        while True:
            game.background_display()
            game.draw_board()
            game.fill_board(board.board)
            game.get_mouse_pos()
            game.get_mouse_click()
            if player.sign == 'O':
                player_moves = len([x for x in board.board if x in player.sign])
                bot_moves = len([x for x in board.board if x in bot.sign])
                if game_state:
                    game.player_move(board, player.sign)
                player_win = board.check_win(player.sign)
                tie = board.tie()
                if player_win:
                    end(board.board, 'Wygrana', player_win[1])
                    game_state = False
                if tie and not (player_win or bot_win):
                    end(board.board, 'Remis', [False])
                    game_state = False
                if player_moves > bot_moves and game_state:
                    board.update_board(bot.move(board.board, player.sign), bot.sign)
                bot_win = board.check_win(bot.sign)
                tie = board.tie()
                if bot_win:
                    end(board.board, 'Przegrana', bot_win[1])
                    game_state = False
                if tie and not (player_win or bot_win):
                    end(board.board, 'Remis', [False])
                    game_state = False
            else:
                if move == 0:
                    board.update_board(bot.move(board.board, player.sign), bot.sign)
                move = 1
                player_moves = len([x for x in board.board if x in player.sign])
                bot_moves = len([x for x in board.board if x in bot.sign])
                if player_moves == bot_moves and game_state:
                    board.update_board(bot.move(board.board, player.sign), bot.sign)
                bot_win = board.check_win(bot.sign)
                tie = board.tie()
                if bot_win:
                    end(board.board, 'Przegrana', bot_win[1])
                    game_state = False
                if tie and not (player_win or bot_win):
                    end(board.board, 'Remis', [False])
                    game_state = False
                if game_state:
                    game.player_move(board, player.sign)
                player_win = board.check_win(player.sign)
                tie = board.tie()
                if player_win:
                    end(board.board, 'Wygrana', player_win[1])
                    game_state = False
                if tie and not (player_win or bot_win):
                    end(board.board, 'Remis', [False])
                    game_state = False
            game.events()
            game.display_update()

    def main_menu():
        while True:
            game.get_mouse_click()
            game.get_mouse_pos()
            game.background_display()
            game.message_display('Kółko i krzyżyk', 'Mistral', 40, game.colors['blue'], (game.center[0], 85))
            game.message_display(f'Poziom trudności:    {difficulty[bot.difficulty]}', 'Mistral', 20, game.colors['blue'], (game.center[0] - 40, game.center[1] - 75))
            game.message_display(f'Znak:    {player.sign}', 'Mistral', 20, game.colors['blue'], (game.center[0] - 12, game.center[1] - 36))
            game.message_display('Zmień znak: ', 'Mistral', 20, game.colors['blue'], (game.center[0], game.center[1] + 4))
            game.button_display('X', game.center[0] - 50, game.center[1] + 7, 50, 30, player.sign_change_x)
            game.button_display('O', game.center[0], game.center[1] + 7, 50, 30, player.sign_change_o)
            game.message_display('Zmień trudność: ', 'Mistral', 20, game.colors['blue'], (game.center[0], game.center[1] + 60))
            game.button_display('ŁATWY', game.center[0] - 100, game.center[1] + 65, 50, 30, bot.difficulty_up, args=(0,))
            game.button_display('ŚREDNI', game.center[0] - 50, game.center[1] + 65, 50, 30, bot.difficulty_up, args=(1,))
            game.button_display('TRUDNY', game.center[0], game.center[1] + 65, 50, 30, bot.difficulty_up, args=(2,))
            game.button_display('EXPERT', game.center[0] + 50, game.center[1] + 65, 50, 30, bot.difficulty_up, args=(3,))

            if player.sign == 'X':
                bot.sign = 'O'
            else:
                bot.sign = 'X'

            game.button_display('START', game.center[0] + 100, game.center[1] + 100, 80, 60, game_loop, args=(True,))
            game.events()
            game.display_update()

    def end(board_list: list, state: str, win: list):
        while True:
            game.background_display()
            game.draw_board()
            game.fill_board(board_list)
            game.get_mouse_click()
            game.get_mouse_pos()

            if state == 'Remis':
                game.message_display(state, 'Mistral', 40, game.colors['blue'], (game.center[0], game.center[1] + 100))
            elif state == 'Wygrana':
                game.message_display(state, 'Mistral', 40, game.colors['green'], (game.center[0], game.center[1] + 100))
            elif state == 'Przegrana':
                game.message_display(state, 'Mistral', 40, game.colors['red'], (game.center[0], game.center[1] + 100))

            if win == [0, 1, 2]:
                game.win_line((135, 225), (315, 225))
            elif win == [3, 4, 5]:
                game.win_line((135, 165), (315, 165))
            elif win == [6, 7, 8]:
                game.win_line((135, 105), (315, 105))
            elif win == [0, 3, 6]:
                game.win_line((165, 80), (165, 255))
            elif win == [1, 4, 7]:
                game.win_line((225, 80), (225, 255))
            elif win == [2, 5, 8]:
                game.win_line((285, 80), (285, 255))
            elif win == [2, 4, 6]:
                game.win_line((135, 80), (315, 255))
            elif win == [0, 4, 8]:
                game.win_line((315, 80), (135, 255))

            game.button_display('MENU', game.center[0] + 100, game.center[1] + 100, 80, 60, main)
            game.events()
            game.display_update()

    board = Board()
    player = Player()
    bot = Bot(board.win_combo)
    difficulty = {0: 'Łatwy', 1: 'Średni', 2: 'Trudny', 3: 'Expert'}
    game = Game()
    game.init()
    game.draw_board()
    main_menu()


if __name__ == "__main__":
    main()
