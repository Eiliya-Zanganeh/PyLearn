import arcade

from food import Apple, Pear, Stone
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Snake Game 🐍")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake = Snake(self.width, self.height)
        self.foods = [Apple(self.width, self.height), Pear(self.width, self.height), Stone(self.width, self.height)]
        self.game_over = False

    def on_draw(self):
        arcade.start_render()
        if self.game_over:
            arcade.draw_text("Game Over :|", self.width // 2, self.height // 2,
                             arcade.color.RED, font_size=30, anchor_x="center")
        else:
            arcade.draw_text(str(self.snake.score), self.width - 40, 40, arcade.color.WHITE, font_size=30,
                             anchor_x="center")
            self.snake.draw()
            for food in self.foods:
                food.draw()
        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        self.snake.change_direction(symbol)

    def on_update(self, delta_time: float):
        self.snake.move()
        if ((self.snake.score < 0) or (self.snake.center_x > self.width) or
                (self.snake.center_x < 0) or (self.snake.center_y > self.height) or
                (self.snake.center_y < 0)):
            self.game_over = True
        for num, body in enumerate(self.snake.body):
            if arcade.check_for_collision(self.snake, body):
                if len(self.snake.body) - 20 < num:
                    continue
                self.game_over = True
        for food in self.foods:
            if arcade.check_for_collision(food, self.snake):
                self.foods = self.snake.eat(food, self.foods)


def main():
    game = Game()
    arcade.run()


if __name__ == "__main__":
    main()
