import arcade

COLUMN_SPACING = 30
ROW_SPACING = 30
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110

arcade.open_window(500, 500, "Eiliya :|")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
is_blue = True
for row in range(10):

    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        if column == 9:
            if is_blue:
                arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.BLUE, tilt_angle=45)
            else:
                arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.RED, tilt_angle=45)
            continue
        if is_blue:
            arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.BLUE, tilt_angle=45)
            is_blue = False
        else:
            arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.RED, tilt_angle=45)
            is_blue = True

arcade.finish_render()

arcade.run()
