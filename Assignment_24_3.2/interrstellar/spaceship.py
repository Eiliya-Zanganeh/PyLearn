import arcade

from bullet import Bullet


class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width = 50
        self.height = 50
        self.center_x = game.width // 2
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0
        self.speed = 8
        self.game_width = game.width
        self.bullets = []

    def move(self):
        if self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed
        elif self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

    def change_move(self, symbol):
        if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.change_x = 1
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.change_x = -1
        elif symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.change_x = 0

    def fire(self):
        new_bullet = Bullet(self)
        self.bullets.append(new_bullet)
