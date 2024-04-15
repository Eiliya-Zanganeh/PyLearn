import time
import arcade
from spaceship import Spaceship
from bad_spaceship import BadSpaceship


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=700, title="Eiliya Game...")
        arcade.set_background_color(arcade.color.BLACK)
        # self.background = arcade.load_texture("/home/eiliya/Desktop/Python/Arcade/img.jpg")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.spaceship = Spaceship(self)
        self.bad_spaceships = []
        self.start_time = time.time()
        self.time_space = 3
        self.bad_spaceships_start_speed = 4
        self.speed_step_bad_spaceships = 0.5
        self.life = 3
        self.life_background = arcade.load_texture(":resources:images/items/flagGreen2.png")
        self.game_over = False
        self.score = 0
        self.sound = arcade.load_sound(":resources:sounds/hit3.wav")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        if self.game_over:
            arcade.draw_text("Game Over :|", self.width // 2, self.height // 2,
                             arcade.color.RED, font_size=30, anchor_x="center")
        else:
            for num in range(self.life):
                arcade.draw_lrwh_rectangle_textured((num * 50) + 10, 20, 50, 50, self.life_background)
            for bad_ship in self.bad_spaceships:
                bad_ship.draw()
            for bullet in self.spaceship.bullets:
                bullet.draw()
            arcade.draw_text(str(self.score), self.width - 40, 40, arcade.color.WHITE, font_size=30, anchor_x="center")
            self.spaceship.draw()
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        self.spaceship.change_move(symbol)
        if symbol == arcade.key.SPACE:
            self.spaceship.fire()

    def on_key_release(self, symbol, modifiers):
        self.spaceship.change_x = 0

    def update(self, delta_time: float):
        for bad_ship in self.bad_spaceships:
            if arcade.check_for_collision(bad_ship, self.spaceship):
                self.game_over = True
                # print("Game Over :|")
                # arcade.close_window()
                # exit(0)

        for bullet in self.spaceship.bullets:
            for bad_ship in self.bad_spaceships:
                if arcade.check_for_collision(bullet, bad_ship):
                    self.spaceship.bullets.remove(bullet)
                    self.bad_spaceships.remove(bad_ship)
                    arcade.play_sound(self.sound)
                    self.score += 1

        for bullet in self.spaceship.bullets:
            bullet.move()

        for bad_ship in self.bad_spaceships:
            if bad_ship.center_y < 0:
                self.bad_spaceships.remove(bad_ship)
                self.life -= 1
                if self.life == 0:
                    self.game_over = True

        for bullet in self.spaceship.bullets:
            if bullet.center_y > self.width:
                self.spaceship.bullets.remove(bullet)

        current_time = time.time()
        # if (random.randint(1, 100) == 100):
        if current_time - self.start_time >= self.time_space:
            new_bad_ship = BadSpaceship(self, self.bad_spaceships_start_speed)
            self.bad_spaceships.append(new_bad_ship)
            self.start_time = current_time
            self.bad_spaceships_start_speed += self.speed_step_bad_spaceships

        for bad_ship in self.bad_spaceships:
            bad_ship.move()

        self.spaceship.move()


window = Game()
arcade.run()
