class Button:
    def __init__(self, message: object, pygame: object, screen: object):
        self.__message = message
        self.__pygame = pygame
        self.__screen = screen

    def _draw(self, text: str, where: object, color: tuple, font_size: int, text_color: tuple, position: tuple, fill=False):
        if fill:
            self.__pygame.draw.rect(where, color, position)
        else:
            self.__pygame.draw.rect(where, color, position, 1)
        self.__message.display(text, "monospace", font_size, text_color, (position[0] + position[2] / 2, position[1] + position[3] / 2))

    def display(self, name, x, y, w, h, fun, mouse_pos, mouse_click,
                args=None,
                active_color=(255, 255, 255),
                passive_color=(255, 255, 255),
                active_text_color=(0, 0, 0),
                passive_text_color=(255, 255, 255),
                passive_fill=False):
        text = h // 2
        if x < mouse_pos[0] < x + w and y < mouse_pos[1] < y + h:
            self._draw(name, self.__screen, active_color, int(text + text * 0.2), active_text_color, (x, y, w, h), fill=not passive_fill)
            if mouse_click[0] == 1:
                if args:
                    fun(args)
                else:
                    fun()
        else:
            self._draw(name, self.__screen, passive_color, text, passive_text_color, (x, y, w, h), fill=passive_fill)
