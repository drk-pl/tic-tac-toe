from src.classes.board_class import Board
from src.classes.player_class import Player
from src.classes.bot_class import Bot
from src.classes.game_class import Game
from src.classes.language_dict import language


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
    global lang, difficulty
    while True:
        difficulty = {0: current_lang['easy'], 1: current_lang['medium'], 2: current_lang['hard'], 3: current_lang['expert']}
        game.get_mouse_click()
        game.get_mouse_pos()
        game.background_display()
        game.message_display(current_lang['title'], 'Mistral', 40, game.colors['blue'], (game.center[0], 85))
        game.message_display(f"{current_lang['difficulty']}:", 'Mistral', 20, game.colors['blue'], (game.center[0], game.center[1] - 58))
        game.message_display(f"{difficulty[bot.difficulty].upper()}", 'Mistral', 18, game.colors['blue'], (game.center[0], game.center[1] - 35))
        game.button_display(f"{current_lang['change'].upper()}", game.center[0] + 80, game.center[1] - 47, 50, 30, bot.difficulty_up)
        game.message_display(f"{current_lang['sign']}:", 'Mistral', 20, game.colors['blue'], (game.center[0], game.center[1] + 2))
        game.message_display(f"{player.sign}", 'Mistral', 18, game.colors['blue'], (game.center[0], game.center[1] + 24))
        game.button_display(f"{current_lang['change'].upper()}", game.center[0] + 80, game.center[1] + 10, 50, 30, player.sign_change)
        game.message_display(f"{current_lang['language']}:", 'Mistral', 20, game.colors['blue'], (game.center[0], game.center[1] + 60))
        game.message_display(f"{current_lang['current_language'].upper()}", 'Mistral', 18, game.colors['blue'], (game.center[0], game.center[1] + 82))
        game.button_display(f"{current_lang['change'].upper()}", game.center[0] + 80, game.center[1] + 70, 50, 30, lang_change)
        if player.sign == 'X':
            bot.sign = 'O'
        else:
            bot.sign = 'X'
        game.button_display(f"{current_lang['start'].upper()}", game.center[0] + 90, game.center[1] + 110, 80, 60, game_loop, args=(True,))
        game.events()
        game.display_update()


def end(board_list: list, state: str, win: list):
    while True:
        game.screen_fill(game.colors['black'])
        game.background_display()
        game.draw_board()
        game.fill_board(board_list)
        game.get_mouse_click()
        game.get_mouse_pos()

        if state == current_lang['tie'].upper():
            game.message_display(state.capitalize(), 'Mistral', 40, game.colors['blue'], (game.center[0] + len(state) // 2, game.center[1] + 100))
        elif state == current_lang['win'].upper():
            game.message_display(state.capitalize(), 'Mistral', 40, game.colors['green'], (game.center[0] + len(state) // 2, game.center[1] + 100))
        elif state == current_lang['lost'].upper():
            game.message_display(state.capitalize(), 'Mistral', 40, game.colors['red'], (game.center[0] + len(state) // 2, game.center[1] + 100))

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
        game.button_display(f"{current_lang['menu'].upper()}", game.center[0] - 140, game.center[1] + 110, 80, 60, main)
        game.button_display(f"{current_lang['again'].upper()}", game.center[0] + 90, game.center[1] + 110, 80, 60, again)
        game.events()
        game.display_update()


def main(reset=True):
    if reset:
        board.reset()
        # game.init()
    main_menu()


def again():
    board.reset()
    game_loop(True)


def lang_change():
    global lang, current_lang
    if lang == 'english':
        lang = 'polish'
    elif lang == 'polish':
        lang = 'english'
    current_lang = language[lang]
    game.caption_change(current_lang)


lang = 'english'
current_lang = language[lang]  
board = Board()
player = Player()
bot = Bot(board.win_combo)
difficulty = {0: current_lang['easy'], 1: current_lang['medium'], 2: current_lang['hard'], 3: current_lang['expert']}
game = Game()
game.init(current_lang)

if __name__ == "__main__":
    main()
