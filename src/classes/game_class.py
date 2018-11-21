import pygame
from pygame.locals import *
import sys
import os


def resource_path(relative_path):
    try:
        base_path = os.path.join(sys._MEIPASS, 'img')
    except Exception:
        base_path = os.path.abspath(os.path.join("..", "img"))

    return os.path.join(base_path, relative_path)


background = resource_path('background.jpg')


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
        self.__mouse_pos = ()
        self.__mouse_click = ()
        self.__images = {'background': self.__pygame.image.load(background)}
        self.__clock = self.__pygame.time.Clock()
        self.__font_type = 'Mistral'

    @property
    def mouse_pos(self) -> tuple:
        return self.__mouse_pos

    @property
    def mouse_click(self) -> tuple:
        return self.__mouse_click

    @mouse_click.setter
    def mouse_click(self, val: tuple):
        self.__mouse_click = val

    @property
    def colors(self) -> dict:
        return self.__colors

    @property
    def center(self) -> tuple:
        return self.__center

    def screen_fill(self, clr):
        self.__screen.fill(clr)

    def get_mouse_pos(self):
        self.__mouse_pos = self.__pygame.mouse.get_pos()

    def get_mouse_click(self):
        self.__mouse_click = self.__pygame.mouse.get_pressed()

    def background_display(self):
        self.__screen.blit(self.__images['background'], (0, 0))

    def init(self, lang: dict):
        self.__pygame.init()
        self.__screen = self.__pygame.display.set_mode((self.__resolution['width'], self.__resolution['height']))
        self.__pygame.display.set_caption(lang['title'])

    def caption_change(self, lang: dict):
        self.__pygame.display.set_caption(lang['title'])

    def win_line(self, start_pos: tuple, end_pos: tuple):
        self.__pygame.draw.line(self.__screen, self.__colors['red'], start_pos, end_pos, 4)

    def fill_board(self, board: list):
        self.message_display(board[6], self.__font_type, 30, self.__colors['blue'], (self.__center[0] - 60, self.__center[1] - 90))
        self.message_display(board[3], self.__font_type, 30, self.__colors['blue'], (self.__center[0] - 60, self.__center[1] - 30))
        self.message_display(board[0], self.__font_type, 30, self.__colors['blue'], (self.__center[0] - 60, self.__center[1] + 30))
        self.message_display(board[7], self.__font_type, 30, self.__colors['blue'], (self.__center[0], self.__center[1] - 90))
        self.message_display(board[4], self.__font_type, 30, self.__colors['blue'], (self.__center[0], self.__center[1] - 30))
        self.message_display(board[1], self.__font_type, 30, self.__colors['blue'], (self.__center[0], self.__center[1] + 30))
        self.message_display(board[8], self.__font_type, 30, self.__colors['blue'], (self.__center[0] + 60, self.__center[1] - 90))
        self.message_display(board[5], self.__font_type, 30, self.__colors['blue'], (self.__center[0] + 60, self.__center[1] - 30))
        self.message_display(board[2], self.__font_type, 30, self.__colors['blue'], (self.__center[0] + 60, self.__center[1] + 30))

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

    def message_display(self, text, font_type, size, clr, pos):
        my_font = self.__pygame.font.SysFont(font_type, size)
        label = my_font.render(text, 1, clr)
        label_rect = label.get_rect(center=pos)
        self.__screen.blit(label, label_rect)

    def button_display(self, name: str, x: int, y: int, w: int, h: int, fun, args=None):
        text = h // 2
        if x < self.__mouse_pos[0] < x + w and y < self.__mouse_pos[1] < y + h:
            self.message_display(name, self.__font_type, int(text + text * 0.2), self.__colors['red'], (x + w / 2, y + h / 3))
            if self.__mouse_click[0] == 1:
                br = False
                while not br:
                    events = self.__pygame.event.get()
                    for e in events:
                        if e.type == MOUSEBUTTONUP:
                            if args:
                                fun(*args)
                                br = True
                            else:
                                fun()
                                br = True
        else:
            self.message_display(name, self.__font_type, text, self.__colors['blue'], (x + w / 2, y + h / 3))
