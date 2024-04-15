import random
import arcade


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 219
        self.center_y = 250
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.speed = 3
        self.color = arcade.color.AMAZON
        self.radius = 10
        self.width = self.radius * 2
        self.height = self.radius * 2

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
