from src.classes.message_class import Message
from src.classes.button_class import Button
import pygame
from pygame.locals import *
import sys


class Game:

    def __init__(self):
        self.__pygame = pygame
        self.__resolution = {'width': 450,
                             'height': 399}
        self.__center = (self.__resolution['width'] // 2, self.__resolution['height'] // 2)
        self.__colors = {'white': (255, 255, 255),
                         'black': (0, 0, 0),
                         'red': (255, 0, 0),
                         'gray': (183, 193, 204),
                         'yellow': (249, 217, 54),
                         'blue': (0, 15, 85),
                         'green': (50, 205, 50)}
        self.__message = ''
        self.__button = ''
        self.__screen = ''
        self.__mouse_pos = ''
        self.__mouse_click = ''
        self.__images = {'background': self.__pygame.image.load('../img/background.jpg')}
        self.__clock = self.__pygame.time.Clock()

    @property
    def mouse_pos(self):
        return self.__mouse_pos

    @property
    def mouse_click(self):
        return self.__mouse_click

    @mouse_click.setter
    def mouse_click(self, val: tuple):
        self.__mouse_click = val

    @property
    def colors(self):
        return self.__colors

    @property
    def center(self):
        return self.__center

    def screen_fill(self, clr):
        self.__screen.fill(clr)

    def get_mouse_pos(self):
        self.__mouse_pos = self.__pygame.mouse.get_pos()

    def get_mouse_click(self):
        self.__mouse_click = self.__pygame.mouse.get_pressed()

    def background_display(self):
        self.__screen.blit(self.__images['background'], (0, 0))

    def init(self):
        self.__pygame.init()
        self.__screen = self.__pygame.display.set_mode((self.__resolution['width'], self.__resolution['height']))
        self.__message = Message(self.__screen, self.__pygame.font)
        self.__button = Button(self.__message, self.__pygame, self.__screen)
        self.__pygame.display.set_caption("Kółko i krzyżyk")

    def message_display(self, text, font_type, size, clr, pos):
        self.__message.display(text, font_type, size, clr, pos)

    def button_display(self, name, x, y, w, h, fun, args=None, passive_fill=False):
        self.__button.display(name, x, y, w, h, fun, self.__mouse_pos, self.__mouse_click, args,
                              passive_fill,
                              active_text_color=self.__colors['red'],
                              passive_text_color=self.__colors['blue'])

    def win_line(self, start_pos: tuple, end_pos: tuple):
        self.__pygame.draw.line(self.__screen, self.__colors['red'], start_pos, end_pos, 4)

    def fill_board(self, board: list):
        self.__message.display(board[6], "Mistral", 30, self.__colors['blue'], (self.__center[0] - 60, self.__center[1] - 90))
        self.__message.display(board[3], "Mistral", 30, self.__colors['blue'], (self.__center[0] - 60, self.__center[1] - 30))
        self.__message.display(board[0], "Mistral", 30, self.__colors['blue'], (self.__center[0] - 60, self.__center[1] + 30))
        self.__message.display(board[7], "Mistral", 30, self.__colors['blue'], (self.__center[0], self.__center[1] - 90))
        self.__message.display(board[4], "Mistral", 30, self.__colors['blue'], (self.__center[0], self.__center[1] - 30))
        self.__message.display(board[1], "Mistral", 30, self.__colors['blue'], (self.__center[0], self.__center[1] + 30))
        self.__message.display(board[8], "Mistral", 30, self.__colors['blue'], (self.__center[0] + 60, self.__center[1] - 90))
        self.__message.display(board[5], "Mistral", 30, self.__colors['blue'], (self.__center[0] + 60, self.__center[1] - 30))
        self.__message.display(board[2], "Mistral", 30, self.__colors['blue'], (self.__center[0] + 60, self.__center[1] + 30))

    def draw_board(self):
        self.__pygame.draw.line(self.__screen, self.__colors['blue'], (self.__center[0] - 30, self.__center[1] - 120), (self.__center[0] - 30, self.__center[1] + 60), 4)
        self.__pygame.draw.line(self.__screen, self.__colors['blue'], (self.__center[0] + 30, self.__center[1] - 120), (self.__center[0] + 30, self.__center[1] + 60), 4)
        self.__pygame.draw.line(self.__screen, self.__colors['blue'], (self.__center[0] - 90, self.__center[1] - 60), (self.__center[0] + 90, self.__center[1] - 60), 4)
        self.__pygame.draw.line(self.__screen, self.__colors['blue'], (self.__center[0] - 90, self.__center[1]), (self.__center[0] + 90, self.__center[1]), 4)

    def events(self):
        events = self.__pygame.event.get()
        for e in events:
            if e.type == QUIT:
                sys.exit(0)
                # quit()

    def display_update(self):
        self.__pygame.display.update()
        self.__clock.tick(60)

    def player_move(self, board: object, player_sign: str):
        self.button_display('', self.__center[0] - 90, self.__center[1] - 120, 60, 60, board.update_board, args=(6, player_sign))
        self.button_display('', self.__center[0] - 90, self.__center[1] - 60, 60, 60, board.update_board, args=(3, player_sign))
        self.button_display('', self.__center[0] - 90, self.__center[1], 60, 60, board.update_board, args=(0, player_sign))
        self.button_display('', self.__center[0] - 30, self.__center[1] - 120, 60, 60, board.update_board, args=(7, player_sign))
        self.button_display('', self.__center[0] - 30, self.__center[1] - 60, 60, 60, board.update_board, args=(4, player_sign))
        self.button_display('', self.__center[0] - 30, self.__center[1], 60, 60, board.update_board, args=(1, player_sign))
        self.button_display('', self.__center[0] + 30, self.__center[1] - 120, 60, 60, board.update_board, args=(8, player_sign))
        self.button_display('', self.__center[0] + 30, self.__center[1] - 60, 60, 60, board.update_board, args=(5, player_sign))
        self.button_display('', self.__center[0] + 30, self.__center[1], 60, 60, board.update_board, args=(2, player_sign))
