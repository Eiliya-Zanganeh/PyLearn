import arcade
import pandas as pd
import numpy as np
from keras.models import load_model

from apple import Apple
from snake import Snake
from config import *


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title="Snake Game 🐍")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake = Snake(self.width, self.height)
        self.foods = [Apple(APPLE_IMAGE, self.width, self.height)]
        self.game_over = False
        if COLLECT_DATASET and MODE == 'AI':
            self.dataset = pd.DataFrame(columns=['SX', 'SY', 'AX', 'AY', 'D'])
        if MODE == 'ML':
            self.model = load_model('results/model.keras')

    def on_draw(self):
        arcade.start_render()
        if self.game_over:
            arcade.draw_text("Game Over :|", self.width // 2, self.height // 2, arcade.color.RED, font_size=30,
                             anchor_x="center")
            self.dataset.to_csv(SAVE_DATASET, index=False)
            arcade.close_window()
            exit(0)
        else:
            arcade.draw_text(str(self.snake.score), self.width - 40, 40, arcade.color.WHITE, font_size=30,
                             anchor_x="center")
            self.snake.draw()
            for food in self.foods:
                food.draw()
        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        if COLLECT_DATASET:
            if symbol == arcade.key.Q:
                self.dataset.to_csv(SAVE_DATASET, index=False)
                arcade.close_window()
                exit(0)

        if MODE == 'Manual':
            self.snake.change_direction(symbol)

    def on_update(self, delta_time: float):
        self.snake.move()
        if ((self.snake.score < 0) or (self.snake.center_x > self.width) or
                (self.snake.center_x < 0) or (self.snake.center_y > self.height) or
                (self.snake.center_y < 0)):
            self.game_over = True
        # for num, body in enumerate(self.snake.body):
        #     if arcade.check_for_collision(self.snake, body):
        #         if len(self.snake.body) - 20 < num:
        #             continue
        #         self.game_over = True
        for food in self.foods:
            if arcade.check_for_collision(food, self.snake):
                self.foods = self.snake.eat(food, self.foods)

        if MODE == 'AI':
            direction = None
            if self.snake.center_y > self.foods[0].center_y:
                self.snake.change_x = 0
                self.snake.change_y = -1
                direction = 0
            elif self.snake.center_y < self.foods[0].center_y:
                self.snake.change_x = 0
                self.snake.change_y = 1
                direction = 1
            elif self.snake.center_x > self.foods[0].center_x:
                self.snake.change_x = -1
                self.snake.change_y = 0
                direction = 2
            elif self.snake.center_x < self.foods[0].center_x:
                self.snake.change_x = 1
                self.snake.change_y = 0
                direction = 3
            if COLLECT_DATASET:
                data = [self.snake.center_x, self.snake.center_y, self.foods[0].center_x, self.foods[0].center_y,
                        direction]
                self.dataset.loc[len(self.dataset)] = data
        if MODE == 'ML':
            data = [
                self.snake.center_x / WINDOW_WIDTH,
                self.snake.center_y / WINDOW_HEIGHT,
                self.foods[0].center_x / WINDOW_WIDTH,
                self.foods[0].center_y / WINDOW_HEIGHT
            ]

            data = np.array([data])
            prediction = np.argmax(self.model.predict(data))
            if prediction == 0:
                self.snake.change_x = 0
                self.snake.change_y = -1
            elif prediction == 1:
                self.snake.change_x = 0
                self.snake.change_y = 1
            elif prediction == 2:
                self.snake.change_x = -1
                self.snake.change_y = 0
            elif prediction == 3:
                self.snake.change_x = 1
                self.snake.change_y = 0


def main():
    Game()
    arcade.run()


if __name__ == "__main__":
    main()
