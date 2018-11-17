from src.classes.board_class import Board
from src.classes.player_class import Player
from src.classes.bot_class import Bot
from src.classes.game_class import Game
from pygame.locals import *


def main():
    board = Board()
    player = Player()
    bot = Bot('O', board.win_combo)
    player.sign = 'X'
    win = False
    game = Game()
    game.init()
    player_moves = 0
    bot_moves = 0
    while True:
        game.screen_fill(game.colors['black'])
        game.get_mouse_pos()
        game.get_mouse_click()
        game.message_display(f"{game.mouse_click[0]} - {game.mouse_pos}", 'consolas', 15, game.colors['white'], (200, 20))
        game.message_display(f"player moves: {player_moves} bot moves: {bot_moves}", 'consolas', 15, game.colors['white'], (200, 40))
        game.draw_board(board.board)
        game.player_move(board, player.sign)
        for j in board.board:
            if j == bot.sign:
                bot_moves += 1
        if player_moves > bot_moves:
            board.update_board(bot.move(board.board), bot.sign)
        player_win = board.check_win(player.sign)
        bot_win = board.check_win(bot.sign)
        if player_win:
            game.message_display("Wygrana", 'consolas', 15, game.colors['white'], (200, 40))
        elif bot_win:
            game.message_display("Przegrana", 'consolas', 15, game.colors['white'], (200, 40))

        game.events()
        game.display_update()


if __name__ == "__main__":
    main()
