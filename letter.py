import random

class Letter:

    __speed_range = [0.1,1.0]
    __foreground_color  = (200,200,200)

    def __init__(self, text, init_pos, end_pos, font):

        self.__speed = random.uniform(*Letter.__speed_range)
        self.__position = init_pos
        self.__end_pos = end_pos

        self.__image = font.render(f"{text}", True, Letter.__foreground_color, None)


    def render(self, surface_dst):
        surface_dst.blit(self.__image ,(self.__position.xy))


    def update(self, delta_time):
        self.__position.y += self.__speed * delta_time