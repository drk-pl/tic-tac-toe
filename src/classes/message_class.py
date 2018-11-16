class Message:
    
    def __init__(self, screen, font):
        self.__screen = screen
        self.__font = font

    def display(self, text, font_type, size, clr, pos):
        my_font = self.__font.SysFont(font_type, size)
        label = my_font.render(text, 1, clr)
        label_rect = label.get_rect(center=pos)
        self.__screen.blit(label, label_rect)
