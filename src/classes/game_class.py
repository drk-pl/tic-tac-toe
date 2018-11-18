from src.classes.message_class import Message
from src.classes.button_class import Button
import pygame
from pygame.locals import *


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
        self.__mouse_pos = ''
        self.__mouse_click = ''

    @property
    def mouse_pos(self):
        return self.__mouse_pos

    @property
    def mouse_click(self):
        return self.__mouse_click

    @property
    def colors(self):
        return self.__colors

    def screen_fill(self, clr):
        self.__screen.fill(clr)

    def get_mouse_pos(self):
        self.__mouse_pos = self.__pygame.mouse.get_pos()

    def get_mouse_click(self):
        self.__mouse_click = self.__pygame.mouse.get_pressed()

    def init(self):
        self.__pygame.init()
        self.__screen = self.__pygame.display.set_mode((self.__resolution['width'], self.__resolution['height']))
        self.__message = Message(self.__screen, self.__pygame.font)
        self.__button = Button(self.__message, self.__pygame, self.__screen)

    def message_display(self, text, font_type, size, clr, pos):
        self.__message.display(text, font_type, size, clr, pos)

    def button_display(self, name, x, y, w, h, fun,
                       args=None,
                       active_color=(255, 255, 255),
                       passive_color=(255, 255, 255),
                       active_text_color=(0, 0, 0),
                       passive_text_color=(255, 255, 255),
                       passive_fill=False):
        self.__button.display(name, x, y, w, h, fun, self.__mouse_pos, self.__mouse_click,
                              args,
                              active_color,
                              passive_color,
                              active_text_color,
                              passive_text_color,
                              passive_fill)

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

    def display_update(self):
        self.__pygame.display.update()

    def player_move(self, board: object, player_sign: str):
        self.button_display('', 50, 80, 100, 100, board.update_board, args=(6, player_sign))
        self.button_display('', 50, 180, 100, 100, board.update_board, args=(3, player_sign))
        self.button_display('', 50, 280, 100, 100, board.update_board, args=(0, player_sign))
        self.button_display('', 150, 80, 100, 100, board.update_board, args=(7, player_sign))
        self.button_display('', 150, 180, 100, 100, board.update_board, args=(4, player_sign))
        self.button_display('', 150, 280, 100, 100, board.update_board, args=(1, player_sign))
        self.button_display('', 250, 80, 100, 100, board.update_board, args=(8, player_sign))
        self.button_display('', 250, 180, 100, 100, board.update_board, args=(5, player_sign))
        self.button_display('', 250, 280, 100, 100, board.update_board, args=(2, player_sign))

    def end(self, board: list, state: str):
        self.__screen.fill(self.__colors["black"])
        self.draw_board(board)
        self.message_display(state, 'consolas', 15, self.__colors['white'], (self.__center[0], 40))
        self.events()
        self.display_update()

