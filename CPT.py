import arcade
import os


WIDTH = 640
HEIGHT = 480

current_screen = "main menu"


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    x = 180
    y = 325
    if current_screen == "main menu":
        arcade.set_background_color(arcade.color.GRAY)
        arcade.draw_text("ESCAPE", x, y, arcade.color.RED_DEVIL, 50, 10, "center", 'Veneer', True, False,)
        arcade.draw_text("to the", x + 40, y - 35, arcade.color.BLACK, 25, 200, "center", "veneer", False, False,)
        arcade.draw_text("FUTURE", x + 25, y - 90, arcade.color.WHITE, 40, 10, "center", "Veneer", True, False,)
        arcade.draw_rectangle_filled(WIDTH/2, 175, 200, 50, arcade.color.LIGHT_GRAY)
        arcade.draw_rectangle_filled(WIDTH/2, 100, 200, 50, arcade.color.LIGHT_GRAY)
        arcade.draw_text("PLAY GAME", 225, 165, arcade.color.BLACK, 25, 200)
        arcade.draw_text("INSTRUCTIONS", 225, 90, arcade.color.BLACK, 19, 200)

    if current_screen == "instructions":
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_text("INSTRUCTIONS", 40, 375, arcade.color.WHITE, 50, 200, "left", "Calibri", True, False)
        arcade.draw_line(40, 360, 600, 360, arcade.color.WHITE, 10)
        arcade.draw_text("In this game, you will be using your wits and brains to try to escape through 4 rooms. You will only be using your mouse through the entirety of this game. You will be clicking on different things and trying to use clues to solve puzzles. You can do stuff like fuse clues together and you can double click on them to get more information on it", 60, 320, arcade.color.WHITE, 15, 250, "left", "arial", False, False)
        mouse = arcade.Sprite("images/mouse_png.png", 0.15)
        mouse.center_x = 450
        mouse.center_y = 200
        mouse.draw()


def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "main menu"


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global current_screen
    if current_screen == "main menu":
        if x > 220 and x < 420 and y > 150 and y < 200:
            print ("play game")
        if x > 220 and x < 420 and y > 75 and y < 125:
            current_screen = "instructions"

if __name__ == '__main__':
    setup()
