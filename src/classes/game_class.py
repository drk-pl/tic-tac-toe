import pygame
from pygame.locals import *
import sys
import os


def resource_path(relative_path, sub):
    """
    Function for getting assets paths
    :param relative_path: Name of the asset
    :param sub: subfolder to look for
    :return: path to asset file
    """
    try:
        base_path = os.path.join(sys._MEIPASS, sub)
    except AttributeError:
        base_path = os.path.abspath(os.path.join("..", sub))

    return os.path.join(base_path, relative_path)


background = resource_path('background.jpg', 'img')
font = resource_path('kalam.ttf', 'font')


class Game:

    __colors = {'white': (255, 255, 255),
                'black': (0, 0, 0),
                'red': (255, 0, 0),
                'gray': (183, 193, 204),
                'yellow': (249, 217, 54),
                'blue': (0, 15, 85),
                'green': (50, 205, 50)}

    __resolution = {'width': 450,
                    'height': 399}

    def __init__(self, title: str, board_size: int, board_pos: tuple, win_combo: list, board_fields_count=(3, 3)):
        """
        Init method of game class. It provides initial parameters for starting game. It requires Board class instance before calling this method.

        :param title: screen caption
        :param board_size: size of a playing board
        :param board_pos: board position on the screen (pixel wise)
        :param win_combo: list of win possibilities (stored in board class)
        :param board_fields_count: dimensions of the board
        :return: NoneType
        """
        self.__pygame = pygame
        self.__center = (self.__resolution['width'] // 2, self.__resolution['height'] // 2)
        self.__mouse_pos = ()
        self.__mouse_click = ()
        self.__images = {'background': self.__pygame.image.load(background)}
        self.__clock = self.__pygame.time.Clock()
        self.__font_type = font
        self.__fps = 60
        self.__fields_order = [6, 7, 8, 3, 4, 5, 0, 1, 2]
        self.__pygame.init()
        self.__screen = self.__pygame.display.set_mode((self.__resolution['width'], self.__resolution['height']))
        self.__pygame.display.set_caption(title)
        self.__board_size = board_size
        self.__board_pos = board_pos
        self.__board_fields_count = board_fields_count
        self.__win_combo = win_combo
        self.__field_size = self.__get_field_size()
        self.__fields_pos = self.__get_fields_pos()
        self.__grid_pos = self.__get_grid_pos()
        self.__win_line_pos = {
            (0, 1, 2): {'start': (self.__fields_pos[0][0], self.__fields_pos[0][1] + self.__field_size[0] // 2),
                        'end': (self.__fields_pos[2][0] + self.__field_size[0], self.__fields_pos[2][1] + self.__field_size[0] // 2)},
            (3, 4, 5): {'start': (self.__fields_pos[3][0], self.__fields_pos[3][1] + self.__field_size[0] // 2),
                        'end': (self.__fields_pos[5][0] + self.__field_size[0], self.__fields_pos[5][1] + self.__field_size[0] // 2)},
            (6, 7, 8): {'start': (self.__fields_pos[6][0], self.__fields_pos[6][1] + self.__field_size[0] // 2),
                        'end': (self.__fields_pos[8][0] + self.__field_size[0], self.__fields_pos[8][1] + self.__field_size[0] // 2)},
            (0, 3, 6): {'start': (self.__fields_pos[0][0] + self.__field_size[1] // 2, self.__fields_pos[0][1] + self.__field_size[0]),
                        'end': (self.__fields_pos[6][0] + self.__field_size[1] // 2, self.__fields_pos[6][1])},
            (1, 4, 7): {'start': (self.__fields_pos[1][0] + self.__field_size[1] // 2, self.__fields_pos[1][1] + self.__field_size[0]),
                        'end': (self.__fields_pos[7][0] + self.__field_size[1] // 2, self.__fields_pos[7][1])},
            (2, 5, 8): {'start': (self.__fields_pos[2][0] + self.__field_size[1] // 2, self.__fields_pos[2][1] + self.__field_size[0]),
                        'end': (self.__fields_pos[8][0] + self.__field_size[1] // 2, self.__fields_pos[8][1])},
            (2, 4, 6): {'start': (self.__fields_pos[2][0] + self.__field_size[0], self.__fields_pos[2][1] + self.__field_size[1]),
                        'end': (self.__fields_pos[6][0], self.__fields_pos[6][1])},
            (0, 4, 8): {'start': (self.__fields_pos[0][0], self.__fields_pos[0][1] + self.__field_size[1]),
                        'end': (self.__fields_pos[8][0] + self.__field_size[0], self.__fields_pos[8][1])}
        }

    @property
    def mouse_pos(self) -> tuple:
        """
        Public access to mouse position
        :return: Tuple with mouse position coordinates
        """
        return self.__mouse_pos

    @property
    def mouse_click(self) -> tuple:
        """
        Public access to mouse pressed buttons
        :return: Tuple with mouse button pressed state
        """
        return self.__mouse_click

    @property
    def colors(self) -> dict:
        """
        Public access to colors dictionary
        :return: Dictionary with colors RGB
        """
        return self.__colors

    @property
    def center(self) -> tuple:
        """
        Public access for center of the screen
        :return: Tuple with center of the screen coordinates (pixel wise)
        """
        return self.__center

    @property
    def fps(self) -> int:
        """
        Public access for FPS constant
        :return: FPS constant
        """
        return self.__fps

    @fps.setter
    def fps(self, new_fps: int):
        """
        Public setter of the FPS constant
        :param new_fps: new FPS number
        :return: NoneType
        """
        self.__fps = new_fps

    # private methods

    def __get_field_size(self):
        """
        Method for getting field size based on init parameters
        :return: tuple with field size x, y
        """
        return self.__board_size // self.__board_fields_count[0], self.__board_size // self.__board_fields_count[1]

    def __get_fields_pos(self):
        """
        Getting every field position based on init parameters
        :return: Dictionary with positions of every fields at index matching board indexes
        """
        fields_pos = []
        field_positions_with_index = {}
        offset = 0
        for row in range(self.__board_fields_count[1]):
            current_field_position = (self.__board_pos[0], self.__board_pos[1] + offset)
            for field in range(self.__board_fields_count[0]):
                current_field_position = (current_field_position[0], current_field_position[1])
                fields_pos.append(current_field_position)
                current_field_position = (current_field_position[0] + self.__field_size[0], current_field_position[1])
            offset += self.__field_size[1]
        for field_index, field_position in zip(self.__fields_order, fields_pos):
            field_positions_with_index[field_index] = field_position
        return field_positions_with_index

    def __get_grid_pos(self):
        """
        Getting the grid lines position based on field positions
        :return: Dictionary with every line positions of the grid
        """
        x_left = self.__fields_pos[0][0]
        x_right = self.__fields_pos[0][0] + self.__board_size
        y_high = self.__fields_pos[6][1]
        y_low = self.__fields_pos[6][1] + self.__board_size
        grid_pos_temp = []
        x_offset = self.__field_size[0]
        y_offset = self.__field_size[1]
        x_pos = self.__board_pos[0]
        y_pos = self.__board_pos[1]
        for line in range(self.__board_fields_count[1] - 1):
            x_pos += x_offset
            grid_pos_temp.append({'start': (x_pos, y_high), 'end': (x_pos, y_low)})
        for line in range(self.__board_fields_count[0] - 1):
            y_pos += y_offset
            grid_pos_temp.append({'start': (x_left, y_pos), 'end': (x_right, y_pos)})
        return grid_pos_temp

    # public methods

    def update_mouse_pos(self):
        """
        Updates mouse position for internal use.
        :return: NoneType
        """
        self.__mouse_pos = self.__pygame.mouse.get_pos()

    def update_mouse_click(self):
        """
        Updates mouse pressed check for internal use.
        :return: NoneType
        """
        self.__mouse_click = self.__pygame.mouse.get_pressed()

    def background_display(self, position=(0, 0)):
        """
        Public method for blitting background image on window.
        :param position: position of image to blit
        :return: NoneType
        """
        self.__screen.blit(self.__images['background'], position)

    def caption_change(self, title: str):
        """
        Method to change screen caption
        :param title: new screen caption
        :return: NoneType
        """
        self.__pygame.display.set_caption(title)

    def win_line(self, win_indexes):
        """
        Drawing win line
        :param win_indexes: list of field indexes that scored win
        :return: NoneType
        """
        self.__pygame.draw.line(self.__screen, self.__colors['red'], self.__win_line_pos[tuple(win_indexes)]['start'], self.__win_line_pos[tuple(win_indexes)]['end'], 4)

    def fill_board(self, board: list):
        """
        Displaying fields values on screen board
        :param board: list of board values from Board class
        :return: NoneType
        """
        field_offset = (self.__field_size[0] // 2, self.__field_size[1] // 2)
        for index, field_position in self.__fields_pos.items():
            self.message_display(board[index],
                                 self.__field_size[1] // 2,
                                 self.__colors['blue'],
                                 (field_position[0] + field_offset[0], field_position[1] + field_offset[1]))

    def draw_board(self):
        """
        Drawing grid lines on screen
        :return: NoneType
        """
        for line in self.__grid_pos:
            self.__pygame.draw.line(self.__screen, self.__colors['blue'], line["start"], line["end"], 4)

    def events(self):
        """
        Handling events
        :return: NoneType
        """
        events = self.__pygame.event.get()
        for e in events:
            if e.type == QUIT:
                sys.exit(0)

    def display_update(self):
        """
        Updating the screen and ticking the clock
        :return: NoneType
        """
        self.__pygame.display.update()
        self.__clock.tick(self.__fps)

    def player_move(self, board: object, player_sign: str):
        """
        Drawing buttons for player to click
        :param board: board object needed for updating board fields
        :param player_sign: Player sign to put into board field
        :return:
        """
        for index, field_position in self.__fields_pos.items():
            self.button_display('',
                                field_position[0],
                                field_position[1],
                                self.__field_size[0],
                                self.__field_size[1],
                                board.update_board,
                                args=(index, player_sign))

    def message_display(self, text: str, size: int, clr: tuple, pos: tuple):
        """
        Public method for printing a message onto screen
        :param text: message context
        :param size: font size
        :param clr: font color
        :param pos: position of message on the screen
        :return: NoneType
        """
        my_font = self.__pygame.font.Font(self.__font_type, size)
        label = my_font.render(text, 1, clr)
        label_rect = label.get_rect(center=pos)
        self.__screen.blit(label, label_rect)

    def button_display(self, name: str, x: int, y: int, w: int, h: int, fun, args=None):
        """
        Public method for displaying button onto screen
        :param name: button name
        :param x: x position of button
        :param y: y position of button
        :param w: button width
        :param h: button height
        :param fun: function to run when button is pressed
        :param args: arguments to pass for above function
        :return: NoneType
        """
        text = h // 2
        if x < self.__mouse_pos[0] < x + w and y < self.__mouse_pos[1] < y + h:
            self.message_display(name, int(text + text * 0.2), self.__colors['red'], (x + w / 2, y + h / 3))
            if self.__mouse_click[0] == 1:
                br = False
                while not br:
                    events = self.__pygame.event.get()
                    self.update_mouse_pos()
                    for e in events:
                        if e.type == MOUSEBUTTONUP and x < self.__mouse_pos[0] < x + w and y < self.__mouse_pos[1] < y + h:
                            if args:
                                fun(*args)
                                br = True
                            else:
                                fun()
                                br = True
                        else:
                            br = True
        else:
            self.message_display(name, text, self.__colors['blue'], (x + w / 2, y + h / 3))
