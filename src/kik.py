from src.classes.board_class import Board
from src.classes.player_class import Player
from src.classes.bot_class import Bot
from src.classes.game_class import Game
from src.classes.language_dict import language


def game_loop(state=False):
    """
    Game loop function applying game logic
    :param state:  State of the game
    :return: NoneType
    """
    game_state = state
    bot_win = False
    move = 0
    while True:
        game.background_display()
        game.draw_board()
        game.fill_board(board.board)
        game.update_mouse_pos()
        game.update_mouse_click()
        if player.sign == 'O':
            player_moves = len([x for x in board.board if x in player.sign])
            bot_moves = len([x for x in board.board if x in bot.sign])
            if game_state:
                game.player_move(board, player.sign)
            player_win = board.check_win(player.sign)
            tie = board.tie()
            if player_win:
                end(board.board, current_lang['win'].upper(), player_win[1])
                game_state = False
            if tie and not (player_win or bot_win):
                end(board.board, current_lang['tie'].upper(), [False])
                game_state = False
            if player_moves > bot_moves and game_state:
                board.update_board(bot.move(board.board, player.sign), bot.sign)
            bot_win = board.check_win(bot.sign)
            tie = board.tie()
            if bot_win:
                end(board.board, current_lang['lost'].upper(), bot_win[1])
                game_state = False
            if tie and not (player_win or bot_win):
                end(board.board, current_lang['tie'].upper(), [False])
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
                end(board.board, current_lang['lost'].upper(), bot_win[1])
                game_state = False
            if tie and not (player_win or bot_win):
                end(board.board, current_lang['tie'].upper(), [False])
                game_state = False
            if game_state:
                game.player_move(board, player.sign)
            player_win = board.check_win(player.sign)
            tie = board.tie()
            if player_win:
                end(board.board, current_lang['win'].upper(), player_win[1])
                game_state = False
            if tie and not (player_win or bot_win):
                end(board.board, current_lang['tie'].upper(), [False])
                game_state = False
        game.events()
        game.display_update()


def main_menu():
    """
    Function for displaying main menu screen
    :return: NoneType
    """
    global lang, difficulty
    while True:
        difficulty = {0: current_lang['easy'],
                      1: current_lang['medium'],
                      2: current_lang['hard'],
                      3: current_lang['expert'],
                      4: current_lang['unbeatable']}
        game.update_mouse_click()
        game.update_mouse_pos()
        game.background_display()
        game.message_display(current_lang['title'], 40, game.colors['blue'], (game.center[0], 85))
        game.message_display(f"{current_lang['difficulty']}:", 20, game.colors['blue'], (game.center[0], game.center[1] - 58))
        game.message_display(f"{difficulty[bot.difficulty].upper()}", 18, game.colors['blue'], (game.center[0], game.center[1] - 35))
        game.button_display(f"{current_lang['change'].upper()}", game.center[0] + 80, game.center[1] - 47, 50, 30, bot.difficulty_up)
        game.message_display(f"{current_lang['sign']}:", 20, game.colors['blue'], (game.center[0], game.center[1] + 2))
        game.message_display(f"{player.sign}", 18, game.colors['blue'], (game.center[0], game.center[1] + 24))
        game.button_display(f"{current_lang['change'].upper()}", game.center[0] + 80, game.center[1] + 10, 50, 30, player.sign_change)
        game.message_display(f"{current_lang['language']}:", 20, game.colors['blue'], (game.center[0], game.center[1] + 60))
        game.message_display(f"{current_lang['current_language'].upper()}", 18, game.colors['blue'], (game.center[0], game.center[1] + 82))
        game.button_display(f"{current_lang['change'].upper()}", game.center[0] + 80, game.center[1] + 70, 50, 30, lang_change)
        if player.sign == 'X':
            bot.sign = 'O'
        else:
            bot.sign = 'X'
        game.button_display(f"{current_lang['start'].upper()}", game.center[0] + 90, game.center[1] + 115, 80, 60, game_loop, args=(True,))
        game.events()
        game.display_update()


def end(board_list: list, state: str, win: list):
    """
    Function for displaying end game screen
    :param board_list: list of board field values
    :param state: state of the game (won,lost,tied)
    :param win: list of indexes of win fields
    :return: NoneType
    """
    while True:
        game.background_display()
        game.draw_board()
        game.fill_board(board_list)
        game.update_mouse_click()
        game.update_mouse_pos()
        if len(win) > 1:
            game.win_line(win)

        if state == current_lang['tie'].upper():
            game.message_display(state.capitalize(), 40, game.colors['blue'], (game.center[0] + len(state) + 10 // 2, game.center[1] + 100))
        elif state == current_lang['win'].upper():
            game.message_display(state.capitalize(), 40, game.colors['green'], (game.center[0] + len(state) + 10 // 2, game.center[1] + 100))
        elif state == current_lang['lost'].upper():
            game.message_display(state.capitalize(), 40, game.colors['red'], (game.center[0] + len(state) + 10 // 2, game.center[1] + 100))

        game.button_display(f"{current_lang['menu'].upper()}", game.center[0] - 140, game.center[1] + 115, 80, 60, main)
        game.button_display(f"{current_lang['again'].upper()}", game.center[0] + 90, game.center[1] + 115, 80, 60, again)
        game.events()
        game.display_update()


def main(reset=True):
    """
    Call main menu function with option to reset board field values
    :param reset: Bool value for reset
    :return: NoneType
    """
    if reset:
        board.reset()
    main_menu()


def again():
    """
    Function for starting game loop again after end screen with board fields values reset
    :return: NoneType
    """
    board.reset()
    game_loop(True)


def lang_change():
    """
    Function for changing language of the game
    :return: NoneType
    """
    global lang, current_lang
    if lang == 'english':
        lang = 'polish'
    elif lang == 'polish':
        lang = 'english'
    current_lang = language[lang]
    game.caption_change(current_lang['title'])


lang = 'english'
current_lang = language[lang]
board = Board()
player = Player()
bot = Bot(board.win_combo)
difficulty = {0: current_lang['easy'],
              1: current_lang['medium'],
              2: current_lang['hard'],
              3: current_lang['expert'],
              4: current_lang['unbeatable']}
game = Game(current_lang['title'], 200, (130, 70), board.win_combo)

if __name__ == "__main__":
    main()
