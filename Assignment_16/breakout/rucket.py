import arcade


class Rucket(arcade.Sprite):
    def __init__(self, game_width):
        super().__init__()
        self.center_x = game_width // 2
        self.center_y = 30
        self.change_x = 0
        self.change_y = 0
        self.width = 60
        self.height = 10
        self.speed = 5
        self.color = arcade.color.WHITE

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def move(self, game_width):
        self.center_x += self.change_x * self.speed
        if self.center_x < 30:
            self.center_x = 30
        elif self.center_x > game_width - 30:
            self.center_x = game_width - 30
