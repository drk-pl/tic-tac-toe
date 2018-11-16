from src.classes.board_class import Board
from src.classes.player_class import Player
from src.classes.bot_class import Bot
from src.classes.message_class import Message
from src.classes.button_class import Button
import pygame
from pygame.locals import *


def screen_layout():
    pass


def sign_choose():
    pass


class Game:

    def __init__(self):
        self.__pygame = pygame
        self.__resolution = {'width': 400,
                             'height': 400}
        self.__center = (self.__resolution['width'] // 2, self.__resolution['height'] // 2)
        self.__colors = {'white': (255, 255, 255),
                         'black': (0, 0, 0),
                         'red': (255, 0, 0),
                         'gray': (183, 193, 204),
                         'yellow': (249, 217, 54)}
        self.__message = ''
        self.__button = ''
        self.__screen = ''

    def init(self):
        self.__pygame.init()
        self.__screen = self.__pygame.display.set_mode((self.__resolution['width'], self.__resolution['height']))
        self.__message = Message(self.__screen, self.__pygame.font)
        self.__button = Button(self.__message, self.__pygame, self.__screen)

    def message_display(self, text, font_type, size, clr, pos):
        self.__message.display(text, font_type, size, clr, pos)

    def button_display(self, name, x, y, w, h, fun, mouse_pos, mouse_click,
                args=None,
                active_color=(255, 255, 255),
                passive_color=(255, 255, 255),
                active_text_color=(0, 0, 0),
                passive_text_color=(255, 255, 255),
                passive_fill=False):
        self.__button.display(name, x, y, w, h, fun, mouse_pos, mouse_click,
                              args=None,
                              active_color=(255, 255, 255),
                              passive_color=(255, 255, 255),
                              active_text_color=(0, 0, 0),
                              passive_text_color=(255, 255, 255),
                              passive_fill=False)

    def draw_board(self, board: list):
        self.__pygame.draw.line(self.__screen, self.__colors['yellow'], (self.__center[0] - 50, self.__center[1] - 120), (self.__center[0] - 50, self.__center[1] + 180), 5)
        self.__pygame.draw.line(self.__screen, self.__colors['yellow'], (self.__center[0] + 50, self.__center[1] - 120), (self.__center[0] + 50, self.__center[1] + 180), 5)
        self.__pygame.draw.line(self.__screen, self.__colors['yellow'], (self.__center[0] - 150, self.__center[1] - 20), (self.__center[0] + 150, self.__center[1] - 20), 5)
        self.__pygame.draw.line(self.__screen, self.__colors['yellow'], (self.__center[0] - 150, self.__center[1] + 80), (self.__center[0] + 150, self.__center[1] + 80), 5)
        self.__message.display(board[6], "consolas", 50, self.__colors['white'], (self.__center[0] - 100, self.__center[1] - 70))
        self.__message.display(board[3], "consolas", 50, self.__colors['white'], (self.__center[0] - 100, self.__center[1] + 30))
        self.__message.display(board[0], "consolas", 50, self.__colors['white'], (self.__center[0] - 100, self.__center[1] + 130))
        self.__message.display(board[7], "consolas", 50, self.__colors['white'], (self.__center[0], self.__center[1] - 70))
        self.__message.display(board[4], "consolas", 50, self.__colors['white'], (self.__center[0], self.__center[1] + 30))
        self.__message.display(board[1], "consolas", 50, self.__colors['white'], (self.__center[0], self.__center[1] + 130))
        self.__message.display(board[8], "consolas", 50, self.__colors['white'], (self.__center[0] + 100, self.__center[1] - 70))
        self.__message.display(board[5], "consolas", 50, self.__colors['white'], (self.__center[0] + 100, self.__center[1] + 30))
        self.__message.display(board[2], "consolas", 50, self.__colors['white'], (self.__center[0] + 100, self.__center[1] + 130))

    def events(self):
        events = self.__pygame.event.get()
        for e in events:
            if e.type == QUIT:
                quit()


def main():
    board = Board()
    player = Player()
    win = False
    game = Game()
    game.init()
    while True:
        game.draw_board(board.board)
        game.events()


if __name__ == "__main__":
    main()
