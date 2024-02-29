import arcade


class Rocket(arcade.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.color = color
        self.speed = 4
        self.score = 0

    def move(self, ball, game_height):
        if ball.center_x > game_height // 2:

            if self.center_y > ball.center_y:
                self.change_y = -1

            if self.center_y < ball.center_y:
                self.change_y = 1

            if self.center_y < 60:
                self.center_y = 60

            if self.center_y > game_height - 60:
                self.center_y = game_height - 60

            self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
