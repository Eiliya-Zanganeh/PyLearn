import random
import arcade

from config import *


class Apple(arcade.Sprite):
    def __init__(self, image, width, height):
        super().__init__(image)
        self.width = APPLE_SIZE
        self.height = APPLE_SIZE
        self.center_x = random.randint(50, width - 50) // 8 * 8
        self.center_y = random.randint(50, height - 50) // 8 * 8
        self.change_x, self.change_y = 0, 0
