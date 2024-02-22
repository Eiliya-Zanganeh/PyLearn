import random
import arcade


class BadSpaceship(arcade.Sprite):
    def __init__(self, game, speed):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.width = 50
        self.height = 50
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height + self.width // 2
        self.angle = 180
        self.speed = speed


    def move(self):
        self.center_y -= self.speed
