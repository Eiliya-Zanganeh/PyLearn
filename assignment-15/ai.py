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
        self.nearest_object = get_nearest_object(self.snake, self.foods[0], self.foods[1])

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

    def on_update(self, delta_time: float):
        # print(self.nearest_object)
        food_coordinates = move_to_food(self.snake, self.nearest_object)
        # print(food_coordinates)
        change_move_direction(self.snake, food_coordinates)
        self.snake.move()
        if ((self.snake.score < 0) or (self.snake.center_x > self.width) or
                (self.snake.center_x < 0) or (self.snake.center_y > self.height) or
                (self.snake.center_y < 0)):
            self.game_over = True
        for food in self.foods:
            if arcade.check_for_collision(food, self.snake):
                self.foods = self.snake.eat(food, self.foods)
                self.nearest_object = get_nearest_object(self.snake, self.foods[0], self.foods[1])


def main():
    game = Game()
    arcade.run()


def get_nearest_object(snake: arcade.Sprite, apple: arcade.Sprite, pear: arcade.Sprite):
    apple_coordinates = [abs(snake.center_x - apple.center_x), abs(snake.center_y - apple.center_y)]
    apple_coordinates = apple_coordinates[0] + apple_coordinates[1]
    pear_coordinates = [abs(snake.center_x - pear.center_x), abs(snake.center_y - pear.center_y)]
    pear_coordinates = pear_coordinates[0] + pear_coordinates[1]
    nearest_object = apple if apple_coordinates < pear_coordinates else pear
    return nearest_object


def move_to_food(snake: arcade.Sprite, food: arcade.Sprite):
    food_coordinates = [snake.center_x - food.center_x, snake.center_y - food.center_y]
    if not (food_coordinates[0] < 10 and food_coordinates[0] > -10):
        return ["x", food_coordinates[0]]
    elif not (food_coordinates[1] < 10 and food_coordinates[1] > -10):
        return ["y", food_coordinates[1]]


def change_move_direction(snake: Snake, direction):
    if direction is None:
        print("None")
    else:
        if direction[0] == "x":
            if direction[1] > 0:
                snake.change_direction(arcade.key.LEFT)
            elif direction[1] < 0:
                snake.change_direction(arcade.key.RIGHT)
        elif direction[0] == "y":
            if direction[1] > 0:
                snake.change_direction(arcade.key.DOWN)
            elif direction[1] < 0:
                snake.change_direction(arcade.key.UP)


if __name__ == "__main__":
    main()
