import random

import arcade


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=900, height=800, title="Eiliya Game...")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.spaceship = Spaceship(self)
        self.bad_spaceship = BadSpaceship(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.spaceship.draw()
        self.bad_spaceship.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == 119:  # W
            self.spaceship.center_y += self.spaceship.speed
        elif symbol == 97:  # A
            self.spaceship.center_x -= self.spaceship.speed
        elif symbol == 115:  # S
            self.spaceship.center_y -= self.spaceship.speed
        elif symbol == 100:  # D
            self.spaceship.center_x += self.spaceship.speed
        else:
            print(symbol)

    def update(self, delta_time: float):
        self.bad_spaceship.center_y -= self.bad_spaceship.speed


class Spaceship(arcade.Sprite):
    def __init__(self, game: Game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width = 50
        self.height = 50
        self.center_x = game.width // 2
        self.center_y = 50
        self.speed = 10


class BadSpaceship(arcade.Sprite):
    def __init__(self, game: Game):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.width = 50
        self.height = 50
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height + self.width // 2
        self.angle = 180
        self.speed = 4


window = Game()
arcade.run()