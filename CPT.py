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

    if current_screen == "main menu":
        draw_mainmenu(180, 325)
    elif current_screen == "instructions":
        draw_instruction()
    elif current_screen == "pause screen":
        draw_pausescreen()
    elif current_screen == "room 1":
        draw_room1(430)
    if current_screen == "book":
        draw_book()


def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "main menu"
    if current_screen == "room 1":
        if key == arcade.key.ESCAPE:
            current_screen = "pause screen"


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global current_screen
    if current_screen == "main menu":
        if x > 220 and x < 420 and y > 150 and y < 200:
            current_screen = "room 1"
        if x > 220 and x < 420 and y > 75 and y < 125:
            current_screen = "instructions"
    if current_screen == "pause screen":
        if x > 100 and x < 300 and y > 150 and y < 200:
            current_screen = "main menu"
        if x > 350 and x < 550 and y > 150 and y < 200:
            current_screen = "room 1"
    if current_screen == "room 1":
        if x > 75 and x < 125 and y > 200 and y < 220:
            current_screen = "book"

def draw_instruction():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("INSTRUCTIONS", 40, 375, arcade.color.WHITE, 50, 200, "left", "Calibri", True, False)
    arcade.draw_line(40, 360, 600, 360, arcade.color.WHITE, 10)
    arcade.draw_text(
        "In this game, you will be using your wits and brains to try to escape through 4 rooms. You will only be using your mouse through the entirety of this game. You will be clicking on different things and trying to use clues to solve puzzles. You can do stuff like fuse clues together and you can double click on them to get more information on it",
        60, 320, arcade.color.WHITE, 15, 250, "left", "arial", False, False)
    mouse = arcade.Sprite("images/mouse_png.png", 0.15)
    mouse.center_x = 450
    mouse.center_y = 200
    mouse.draw()

def draw_mainmenu(x, y):
    arcade.set_background_color(arcade.color.GRAY)
    arcade.draw_text("ESCAPE", x, y, arcade.color.RED_DEVIL, 50, 10, "center", 'Veneer', True, False, )
    arcade.draw_text("to the", x + 40, y - 35, arcade.color.BLACK, 25, 200, "center")
    arcade.draw_text("FUTURE", x + 25, y - 90, arcade.color.WHITE, 40, 10, "center", "Veneer", True, False, )
    arcade.draw_rectangle_filled(WIDTH / 2, 175, 200, 50, arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(WIDTH / 2, 100, 200, 50, arcade.color.LIGHT_GRAY)
    arcade.draw_text("PLAY GAME", 225, 165, arcade.color.BLACK, 25, 200)
    arcade.draw_text("INSTRUCTIONS", 225, 90, arcade.color.BLACK, 19, 200)


def draw_pausescreen():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("QUIT GAME?", 77, HEIGHT / 2, arcade.color.WHITE, 50, 500, "center", "Arial", True)
    arcade.draw_rectangle_filled(200, 175, 200, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(450, 175, 200, 50, arcade.color.WHITE)
    arcade.draw_text("QUIT", 155, 165, arcade.color.BLACK, 25, 200)
    arcade.draw_text("RESUME", 385, 165, arcade.color.BLACK, 25, 200)


def draw_room1(whitesquare_x):
    arcade.set_background_color(arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(WIDTH / 2, 40, WIDTH, 80, arcade.color.GRAY)
    arcade.draw_rectangle_filled(570, HEIGHT / 2, 145, HEIGHT, arcade.color.BLACK)
    for _ in range(5):
        arcade.draw_rectangle_filled(570, whitesquare_x, 80, 80, arcade.color.WHITE)
        whitesquare_x -= 95
    arcade.draw_rectangle_filled(260, 155, 75, 150, arcade.color.BROWN)
    arcade.draw_circle_filled(235, 150, 7, arcade.color.GOLD)
    arcade.draw_rectangle_filled(100, 230, 150, 300, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(100, 350, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 290, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 230, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 170, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 110, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 210, 50, 10, arcade.color.RED)


def draw_book():
    arcade.draw_rectangle_filled(WIDTH/2 - 145, HEIGHT/2, WIDTH - 145, HEIGHT, arcade.color.LIGHT_BROWN)


if __name__ == '__main__':
    setup()
