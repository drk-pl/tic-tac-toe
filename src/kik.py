from src.classes.board_class import Board
from src.classes.player_class import Player
from src.classes.bot_class import Bot
from src.classes.game_class import Game


def main():
    board = Board()
    player = Player()
    bot = Bot('O', board.win_combo)
    player.sign = 'X'
    bot.sign = 'O'
    win = False
    game_state = True
    game = Game()
    game.init()
    while True:
        player_moves = len([x for x in board.board if x in player.sign])
        bot_moves = len([x for x in board.board if x in bot.sign])
        game.screen_fill(game.colors['black'])
        game.get_mouse_pos()
        game.get_mouse_click()
        game.message_display(f"player moves: {player_moves} bot moves: {bot_moves}", 'consolas', 15, game.colors['white'], (200, 20))
        game.draw_board(board.board)
        game.player_move(board, player.sign, game_state)
        player_win = board.check_win(player.sign)
        if player_win:
            game.end(board.board, 'Wygrana')
        if player_moves > bot_moves:
            board.update_board(bot.move(board.board), bot.sign, game_state)
        bot_win = board.check_win(bot.sign)
        if bot_win:
            game.end(board.board, 'Przegrana')


        game.events()
        game.display_update()


if __name__ == "__main__":
    main()
