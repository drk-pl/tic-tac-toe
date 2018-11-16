from src.classes.board_class import Board
from src.classes.player_class import Player
from src.classes.bot_class import Bot
from src.classes.message_class import Message
from src.classes.button_class import Button
from pygame import *


def screen_layout():
    pass


def sign_choose():
    pass


def draw_board():
    pass


def main():
    resolution = {'width': 400,
                  'height': 400}
    screen = display.set_mode((resolution['width'], resolution['height']))
    display.set_caption('Kółko i krzyżyk')
    init()
    message = Message(screen, font)
    button = Button(message, pygame, screen)
    board = Board()
    player = Player()
    win = False

    if player.sign == 'X':
        bot = Bot('O', board.win_combo)
    else:
        bot = Bot('X', board.win_combo)

    def player_strike():
        while True:
            place_to_strike = player.move()
            strike = board.update_board(place_to_strike, player.sign)
            if board.check_win(player.sign):
                return True
            if board.tie():
                return True
            if strike:
                break

    def bot_strike():
        print("Ruch przeciwnika: ")
        board.update_board(bot.move(board.board), bot.sign)

        if board.check_win(bot.sign):
            return True
        if board.tie():
            return True

    while not win:
        if player.sign == 'O':
            player_win = player_strike()
            if player_win:
                win = True
                continue
            bot_win = bot_strike()
            if bot_win:
                win = True
                continue
        elif player.sign == 'X':
            bot_win = bot_strike()
            if bot_win:
                win = True
                continue
            player_win = player_strike()
            if player_win:
                win = True
                continue
    if board.check_win(player.sign):
        print("Wygrana")
    elif board.check_win(bot.sign):
        print("Przegrana")
    elif board.tie():
        print("Remis")
    br = False
    while not br:
        again = input("Gramy od nowa? [t/n] ")
        if again.lower() == 't':
            main()
        elif again.lower() == 'n':
            br = True
        else:
            print("Wybierz 't' lub 'n'")


if __name__ == "__main__":
    main()
