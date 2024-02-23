import arcade

from food import Apple, Pear, Stone


class Body(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = x
        self.center_y = y

    def draw(self, color, *args, **kwargs):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, color)


class Snake(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = width // 2
        self.center_y = height // 2
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.color = arcade.color.GREEN
        self.body = []
        self.score = 1
        self.game_width = width
        self.game_height = height

    def change_direction(self, symbol):
        if symbol == arcade.key.UP:
            self.change_y = 1
            self.change_x = 0
        elif symbol == arcade.key.DOWN:
            self.change_y = -1
            self.change_x = 0
        elif symbol == arcade.key.LEFT:
            self.change_x = -1
            self.change_y = 0
        elif symbol == arcade.key.RIGHT:
            self.change_x = 1
            self.change_y = 0

    def eat(self, food, foods):
        if isinstance(food, Apple):
            self.score += 1
            foods[0] = Apple(self.game_width, self.game_height)
        elif isinstance(food, Pear):
            self.score += 2
            foods[1] = Pear(self.game_width, self.game_height)
        elif isinstance(food, Stone):
            self.score -= 1
            foods[2] = Stone(self.game_width, self.game_height)
        return foods

    def move(self):
        body = Body(self.center_x, self.center_y)
        self.body.append(body)
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self, *args, **kwargs):
        is_color = True
        for part in self.body:
            if is_color:
                part.draw(color=arcade.color.APPLE_GREEN)
                is_color = False
            else:
                part.draw(color=self.color)
                is_color = True
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
