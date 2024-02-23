import random
import arcade


class Food(arcade.Sprite):
    def __init__(self, image, width, height):
        super().__init__(image)
        self.width = 32
        self.height = 32
        self.center_x = random.randint(50, width - 50)
        self.center_y = random.randint(50, height - 50)
        self.change_x, self.change_y = 0, 0


class Pear(Food):
    def __init__(self, width, height):
        super().__init__("assets/pear.png", width, height)


class Apple(Food):
    def __init__(self, width, height):
        super().__init__("assets/apple.png", width, height)


class Stone(Food):
    def __init__(self, width, height):
        super().__init__(":resources:images/space_shooter/meteorGrey_big3.png", width, height)
