import random
import arcade
from rucket import Rucket
from block import Block
from ball import Ball


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=438, height=500, title="Breakout :|")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.player = Rucket(self.width)
        self.life = 3
        self.score = 10
        self.blocks = []
        self.life_background = arcade.load_texture(":resources:images/items/flagGreen2.png")
        self.ball = Ball()
        for i in range(15):
            row = []
            color = random.choice(
                [arcade.color.RED, arcade.color.GREEN, arcade.color.BLUE, arcade.color.YELLOW, arcade.color.ORANGE,
                 arcade.color.CHARLESTON_GREEN, arcade.color.SPRING_GREEN, arcade.color.CYAN, arcade.color.AZURE,
                 arcade.color.VIOLET, arcade.color.MAGENTA, arcade.color.ROSE])
            for j in range(10):
                block = Block(self.width - (30 + (42 * j)), self.height - (50 + (12 * i)), color)
                row.append(block)
            self.blocks.append(row)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player.change_x = 0
        self.player.center_x = x

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 1
        elif symbol == arcade.key.LEFT:
            self.player.change_x = -1

    def on_draw(self):
        arcade.start_render()
        if self.life <= 0:
            arcade.draw_text("Game Over :|", self.width // 2, self.height // 2,
                             arcade.color.RED, font_size=30, anchor_x="center")
        else:
            arcade.draw_text(self.score, self.width - 30, self.height - 30)
            for i in range(self.life):
                arcade.draw_lrwh_rectangle_textured((i * 30) + 10, self.height - 30, 20, 20, self.life_background)
            for row in self.blocks:
                for block in row:
                    block.draw()
            self.player.draw()
            self.ball.draw()
        arcade.finish_render()

    def on_update(self, delta_time: float):
        self.ball.move()
        self.player.move(self.width)
        for row in range(len(self.blocks) - 4, len(self.blocks)):
            for block in self.blocks[row]:
                if arcade.check_for_collision(self.ball, block):
                    self.ball.change_y = -1
                    self.blocks[row].remove(block)
                    self.score += 10
            if len(self.blocks[-1]) == 0:
                self.blocks.pop(-1)
        if self.ball.center_x < 0 or self.ball.center_x > self.width:
            self.ball.change_x *= -1

        if arcade.check_for_collision(self.player, self.ball):
            self.ball.change_y = 1

        if self.ball.center_y < 0:
            self.life -= 1
            del self.ball
            self.ball = Ball()


def main():
    game = Game()
    arcade.run()


if __name__ == "__main__":
    main()
