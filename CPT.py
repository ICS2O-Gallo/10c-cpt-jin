import arcade


#Window Dimmensions
WIDTH = 640
HEIGHT = 480

#BUTTON CODE
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3

start_button = [220, 150, 200, 50]
instructions_button = [220, 75, 200, 50]
quit_button = [100, 150, 200, 50]
resume_button = [350, 150, 200, 50]
fuse_button = [100, 25, 200, 10]
unlock_button = [100, 25, 200, 10]

#GAME VARIABLES
current_screen = "main menu"

game = False

#NUMBERCODE
code_number1 = 4
code_number2 = 1
code_number3 = 2
code_number4 = 3

player_input1 = 0
player_input2 = 0
player_input3 = 0
player_input4 = 0

#ITEMS
paper_in_inventory = False
pictureframe_in_inventory = False
screwdriver_in_inventory = False
bluepaper_in_inventory = False
key_in_inventory = False

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
    global player_input1, player_input2, player_input3, player_input4, paper_in_inventory, pictureframe_in_inventory,\
        screwdriver_in_inventory, bluepaper_in_inventory, key_in_inventory
    #RESETS EVERYTIME GAME IS QUIT
    if current_screen == "main menu":
        player_input1 = 0
        player_input2 = 0
        player_input3 = 0
        player_input4 = 0
        paper_in_inventory = False
        pictureframe_in_inventory = False
        screwdriver_in_inventory = False
        bluepaper_in_inventory = False
        key_in_inventory = False


def on_draw():
    arcade.start_render()
    global game
    global paper_in_inventory

    if current_screen == "main menu":
        draw_mainmenu(180, 325)
    elif current_screen == "instructions":
        draw_instruction()
    #ALL THE DIFFERERNT PAUSE SCREENS FOR CERTAIN SCREENS
    elif current_screen == "pause screen1" or current_screen == "pause screen2" or current_screen == "pause screen3"\
            or current_screen == "pause screen4" or current_screen == "pause screen5" or current_screen == "pause screen5"\
            or current_screen == "pause screen6" or current_screen == "pause screen7" or current_screen == "pause screen8"\
            or current_screen == "pause screen9" or current_screen == "pause screen10" or current_screen == "pause screen11"\
            or current_screen == "pause screen12" or current_screen == "pause screen13" or current_screen == "pause screen14"\
            or current_screen == "pause screen15" or current_screen == "pause screen16" or current_screen == "pause screen17"\
            or current_screen == "pause screen18" or current_screen == "pause screen19" or current_screen == "pause screen20"\
            or current_screen == "pause screen21" or current_screen == "pause screen22" or current_screen == "pause screen23"\
            or current_screen == "pause screen24" or current_screen == "pause screen25" or current_screen == "pause screen26"\
            or current_screen == "pause screen27" or current_screen == "pause screen28" or current_screen == "pause screen29"\
            or current_screen == "pause screen30":
        draw_pausescreen()
        game = False
    elif current_screen == "room":
        draw_room()
        game = True
    elif current_screen == "left side":
        draw_leftside()
    elif current_screen == "right side":
        draw_rightside()
    if current_screen == "book":
        draw_book()
    if game is True:
        draw_sidebar(430)
    if current_screen == "locked box":
        draw_lockedbox()
    #DIFFERENT PAPER SCREENS
    if current_screen == "paper1" \
            or current_screen == "paper2"\
            or current_screen == "paper3"\
            or current_screen == "paper4"\
            or current_screen == "paper5":
        draw_paper()
    #DIFFERENT PICTURE FRAME SCREENS
    if current_screen == "pictureframe1" \
            or current_screen == "pictureframe2"\
            or current_screen == "pictureframe3"\
            or current_screen == "pictureframe4"\
            or current_screen == "pictureframe5":
        draw_pictureframe()
    #DIFFERENT SCREW DRIVER SCREENS
    if current_screen == "screwdriver1" \
            or current_screen == "screwdriver2" \
            or current_screen == "screwdriver3" \
            or current_screen == "screwdriver4" \
            or current_screen == "screwdriver5":
        draw_screwdriver()
    #DIFFERENT BLUE PAPER SCREENS
    if current_screen == "bluepaper1" \
            or current_screen == "bluepaper2" \
            or current_screen == "bluepaper3" \
            or current_screen == "bluepaper4" \
            or current_screen == "bluepaper5":
        draw_bluepaper()
    #DIFFERENT KEY SCREENS
    if current_screen == "key1" \
            or current_screen == "key2" \
            or current_screen == "key3" \
            or current_screen == "key4" \
            or current_screen == "key5":
        draw_key(100)

    #VICTORY SCREEN
    if current_screen == "victory":
        draw_victory()

def on_key_press(key, modifiers):
    #MULTIPLE PAUSESCREENS
    global current_screen
    if current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "main menu"
    if game is True:
        #ACCESS TO ALL PAUSE SCREENS
        if current_screen == "room":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen1"
        if current_screen == "book":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen2"
        if current_screen == "locked box":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen3"
        if current_screen == "paper1":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen4"
        if current_screen == "paper2":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen5"
        if current_screen == "paper3":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen6"
        if current_screen == "paper4":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen7"
        if current_screen == "paper5":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen8"
        if current_screen == "left side":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen9"
        if current_screen == "right side":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen10"
        if current_screen == "pictureframe1":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen11"
        if current_screen == "pictureframe2":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen12"
        if current_screen == "pictureframe3":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen13"
        if current_screen == "pictureframe4":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen14"
        if current_screen == "pictureframe5":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen15"
        if current_screen == "screwdriver1":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen16"
        if current_screen == "screwdriver2":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen17"
        if current_screen == "screwdriver3":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen18"
        if current_screen == "screwdriver4":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen19"
        if current_screen == "screwdriver5":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen20"
        if current_screen == "bluepaper1":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen21"
        if current_screen == "bluepaper2":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen22"
        if current_screen == "bluepaper3":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen23"
        if current_screen == "bluepaper4":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen24"
        if current_screen == "bluepaper5":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen25"
        if current_screen == "key1":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen26"
        if current_screen == "key2":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen27"
        if current_screen == "key3":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen28"
        if current_screen == "key4":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen29"
        if current_screen == "key5":
            if key == arcade.key.ESCAPE:
                current_screen = "pause screen30"

    if current_screen == "victory":
        if key == arcade.key.ESCAPE:
            current_screen = "main menu"


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global current_screen, game, paper_in_inventory, pictureframe_in_inventory, screwdriver_in_inventory,\
        bluepaper_in_inventory, key_in_inventory, player_input1, player_input2, player_input3, player_input4

    if game is False:
        #BUTTON PRESSES FOR ALL PAUSE SCREENS
        if current_screen == "main menu":
            if x > start_button[BTN_X] \
                    and x < start_button[BTN_X] + start_button[BTN_WIDTH] \
                    and y > start_button[BTN_Y] \
                    and y < start_button[BTN_Y] + start_button[BTN_HEIGHT]:
                current_screen = "room"
                game = True
            if x > instructions_button[BTN_X] \
                    and x < instructions_button[BTN_X] + instructions_button[BTN_WIDTH] \
                    and y > instructions_button[BTN_Y] \
                    and y < instructions_button[BTN_Y] + instructions_button[BTN_HEIGHT]:
                current_screen = "instructions"
        if current_screen == "pause screen1":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "room"
                    game = True
        if current_screen == "pause screen2":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "book"
                    game = True
        if current_screen == "pause screen3":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "locked box"
                    game = True
        if current_screen == "pause screen4":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "paper1"
                    game = True
        if current_screen == "pause screen5":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "paper2"
                    game = True
        if current_screen == "pause screen6":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "paper3"
                    game = True
        if current_screen == "pause screen7":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "paper4"
                    game = True
        if current_screen == "pause screen8":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "paper5"
                    game = True
        if current_screen == "pause screen9":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "left side"
                    game = True
        if current_screen == "pause screen10":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "right side"
                    game = True
        if current_screen == "pause screen11":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "pictureframe1"
                    game = True
        if current_screen == "pause screen12":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "pictureframe2"
                    game = True
        if current_screen == "pause screen13":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "pictureframe3"
                    game = True
        if current_screen == "pause screen14":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "pictureframe4"
                    game = True
        if current_screen == "pause screen15":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "pictureframe5"
                    game = True
        if current_screen == "pause screen16":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "screwdriver1"
                    game = True
        if current_screen == "pause screen17":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "screwdriver2"
                    game = True
        if current_screen == "pause screen18":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "screwdriver3"
                    game = True
        if current_screen == "pause screen19":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "screwdriver4"
                    game = True
        if current_screen == "pause screen20":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "screwdriver5"
                    game = True
        if current_screen == "pause screen21":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "bluepaper1"
                    game = True
        if current_screen == "pause screen22":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "bluepaper2"
                    game = True
        if current_screen == "pause screen23":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "bluepaper3"
                    game = True
        if current_screen == "pause screen24":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "bluepaper4"
                    game = True
        if current_screen == "pause screen25":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "bluepaper5"
                    game = True
        if current_screen == "pause screen26":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "key1"
                    game = True
        if current_screen == "pause screen27":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "key2"
                    game = True
        if current_screen == "pause screen28":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "key3"
                    game = True
        if current_screen == "pause screen29":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "key4"
                    game = True
        if current_screen == "pause screen30":
            if x > quit_button[BTN_X] \
                    and x < quit_button[BTN_X] + quit_button[BTN_WIDTH] \
                    and y > quit_button[BTN_Y] \
                    and y < quit_button[BTN_Y] + quit_button[BTN_HEIGHT]:
                    current_screen = "main menu"
            if x > resume_button[BTN_X] \
                    and x < resume_button[BTN_X] + resume_button[BTN_WIDTH] \
                    and y > resume_button[BTN_Y] \
                    and y < resume_button[BTN_Y] + resume_button[BTN_HEIGHT]:
                    current_screen = "key5"
                    game = True

    elif game is True:
        #THINGS TO CLICK IN ROOM
        if current_screen == "room":
            if x > 75 and x < 125 and y > 200 and y < 220:
                current_screen = "book"
                game = True
            if x > 380 and x < 440 and y > 170 and y < 200:
                current_screen = "locked box"
                game = True
            if x > 3 and x < 93 and y > 2 and y < 75:
                current_screen = "left side"
                game = True
            if x > 405 and x < WIDTH - 145 and y > 2 and y < 75:
                current_screen = "right side"
                game = True
        #THINGS TO CLICK IN LEFT SIDE
        if current_screen == "left side":
            if x > 405 and x < WIDTH - 145 and y > 2 and y < 75:
                current_screen = "room"
                game = True
            if bluepaper_in_inventory is False:
                if x > 90 and x < 130 and y > 170 and y < 230:
                    pictureframe_in_inventory = True
        #THINGS TO CLICK IN RIGHT SIDE
        if current_screen == "right side":
            if x > 3 and x < 93 and y > 2 and y < 75:
                current_screen = "room"
                game = True
            if bluepaper_in_inventory is False:
                if x > 125 and x < 210 and y > 180 and y < 190:
                    screwdriver_in_inventory = True
        #THINGS TO CLICK IN BOOK
        if current_screen == "book":
            if x > 12 and x < 50 and y > 12 and y < 59:
                paper_in_inventory = True
            if x > 20 and x < 120 and y > 380 and y < 450:
                current_screen = "room"
        #THINGS TO CLICK IN LOCKED BOX
        if current_screen == "locked box":
            if x > 20 and x < 120 and y > 380 and y < 450:
                current_screen = "room"
            #LOCKED BOX BUTTONS
            if x > 130 and x < 170 and y > 240 and y < 255:
                player_input1 += 1
                if player_input1 == 10:
                    player_input1 = 0
            if x > 130 and x < 170 and y > 175 and y <190:
                player_input1 -= 1
                if player_input1 == -1:
                    player_input1 = 9
            if x > 330 and x < 370 and y > 240 and y < 255:
                player_input2 += 1
                if player_input2 == 10:
                    player_input2 = 0
            if x > 330 and x < 370 and y > 175 and y < 190:
                player_input2 -= 1
                if player_input2 == -1:
                    player_input2 = 9
            if x > 130 and x < 170 and y > 150 and y < 165:
                player_input3 += 1
                if player_input3 == 10:
                    player_input3 = 0
            if x > 130 and x < 170 and y > 85 and y < 100:
                player_input3 -= 1
                if player_input3 == -1:
                    player_input3 = 9
            if x > 330 and x < 370 and y > 150 and y < 165:
                player_input4 += 1
                if player_input4 == 10:
                    player_input4 = 0
            if x > 330 and x < 370 and y > 85 and y < 100:
                player_input4 -= 1
                if player_input4 == -1:
                    player_input4 = 9
            #TO UNLOCK LOCKED BOX
            if player_input1 == 4 and player_input2 == 1 and player_input3 == 2 and player_input4 == 3:
                if x > 235 and x < 265 and y > 140 and y < 200:
                    key_in_inventory = True

        if paper_in_inventory is True:
            #ACCESS TO PAPER SCREENS FROM DIFFERENT SCREENS
            if current_screen == "room" or current_screen == "pictureframe1" or current_screen == "screwdriver1" or current_screen == "bluepaper1" or current_screen == "key1":
                if x > 545 and x < 605 and y > 395 and y < 465:
                    current_screen = "paper1"
            if current_screen == "book" or current_screen == "pictureframe2" or current_screen == "screwdriver2" or current_screen == "bluepaper2" or current_screen == "key2":
                if x > 545 and x < 605 and y > 395 and y < 465:
                    current_screen = "paper2"
            if current_screen == "locked box" or current_screen == "pictureframe3" or current_screen == "screwdriver3" or current_screen == "bluepaper3" or current_screen == "key3":
                if x > 545 and x < 605 and y > 395 and y < 465:
                    current_screen = "paper3"
            if current_screen == "left side" or current_screen == "pictureframe4" or current_screen == "screwdriver4" or current_screen == "bluepaper4" or current_screen == "key4":
                if x > 545 and x < 605 and y > 395 and y < 465:
                    current_screen = "paper4"
            if current_screen == "right side" or current_screen == "pictureframe5" or current_screen == "screwdriver5" or current_screen == "bluepaper5" or current_screen == "key5":
                if x > 545 and x < 605 and y > 395 and y < 465:
                    current_screen = "paper5"

        #CODE FOR BACKING OUT OF ITEM SCREENS
        if current_screen == "paper1" or current_screen == "pictureframe1" or current_screen == "screwdriver1" or current_screen == "bluepaper1" or current_screen == "key1":
            if x > 20 and x < 120 and y > 380 and y < 450:
                current_screen = "room"
        if current_screen == "paper2" or current_screen == "pictureframe2" or current_screen == "screwdriver2" or current_screen == "bluepaper2" or current_screen == "key2":
            if x > 20 and x < 120 and y > 380 and y < 450:
                current_screen = "book"
        if current_screen == "paper3" or current_screen == "pictureframe3" or current_screen == "screwdriver3" or current_screen == "bluepaper3" or current_screen == "key3":
            if x > 20 and x < 120 and y > 380 and y < 450:
                current_screen = "locked box"
        if current_screen == "paper4" or current_screen == "pictureframe4" or current_screen == "screwdriver4" or current_screen == "bluepaper4" or current_screen == "key4":
            if x > 20 and x < 120 and y > 380 and y < 450:
                current_screen = "left side"
        if current_screen == "paper5" or current_screen == "pictureframe5" or current_screen == "screwdriver5" or current_screen == "bluepaper5" or current_screen == "key5":
            if x > 20 and x < 120 and y > 380 and y < 450:
                current_screen = "right side"

        if pictureframe_in_inventory is True:
            # ACCESS TO PICTURE FRAME SCREENS FROM DIFFERENT SCREENS
            if current_screen == "room" or current_screen == "paper1" or current_screen == "screwdriver1" or current_screen == "key1":
                if x > 545 and x < 605 and y > 295 and y < 375:
                    current_screen = "pictureframe1"
            if current_screen == "book" or current_screen == "paper2" or current_screen == "screwdriver2" or current_screen == "key2":
                if x > 545 and x < 605 and y > 295 and y < 375:
                    current_screen = "pictureframe2"
            if current_screen == "locked box" or current_screen == "paper3" or current_screen == "screwdriver3" or current_screen == "key3":
                if x > 545 and x < 605 and y > 295 and y < 375:
                    current_screen = "pictureframe3"
            if current_screen == "left side" or current_screen == "paper4" or current_screen == "screwdriver4" or current_screen == "key4":
                if x > 545 and x < 605 and y > 295 and y < 375:
                    current_screen = "pictureframe4"
            if current_screen == "right side" or current_screen == "paper5" or current_screen == "screwdriver5" or current_screen == "key5":
                if x > 545 and x < 605 and y > 295 and y < 375:
                    current_screen = "pictureframe5"

        if screwdriver_in_inventory is True:
            # ACCESS TO SCREWDRIVER SCREENS FROM DIFFERENT SCREENS
            if current_screen == "room" or current_screen == "paper1" or current_screen == "pictureframe1" or current_screen == "key1":
                if x > 545 and x < 605 and y > 200 and y < 280:
                    current_screen = "screwdriver1"
            if current_screen == "book" or current_screen == "paper2" or current_screen == "pictureframe2" or current_screen == "key2":
                if x > 545 and x < 605 and y > 200 and y < 280:
                    current_screen = "screwdriver2"
            if current_screen == "locked box" or current_screen == "paper3" or current_screen == "pictureframe3" or current_screen == "key3":
                if x > 545 and x < 605 and y > 200 and y < 280:
                    current_screen = "screwdriver3"
            if current_screen == "left side" or current_screen == "paper4" or current_screen == "pictureframe4" or current_screen == "key4":
                if x > 545 and x < 605 and y > 200 and y < 280:
                    current_screen = "screwdriver4"
            if current_screen == "right side" or current_screen == "paper5" or current_screen == "pictureframe5" or current_screen == "key5":
                if x > 545 and x < 605 and y > 200 and y < 280:
                    current_screen = "screwdriver5"

        if pictureframe_in_inventory is True and screwdriver_in_inventory is True:
            #GETS RID OF PICTURE FRAME AND SCREWDRIVER AND GET BLUE PAPER
            if current_screen == "pictureframe1" \
                or current_screen == "pictureframe2" \
                or current_screen == "pictureframe3" \
                or current_screen == "pictureframe4" \
                or current_screen == "pictureframe5" \
                or current_screen == "screwdriver1" \
                or current_screen == "screwdriver2" \
                or current_screen == "screwdriver3" \
                or current_screen == "screwdriver4" \
                or current_screen == "screwdriver5":
                if x > fuse_button[BTN_X] and x < 400 and y > fuse_button[BTN_Y] and y < 60:
                    pictureframe_in_inventory = False
                    screwdriver_in_inventory = False
                    bluepaper_in_inventory = True

    if bluepaper_in_inventory is True:
        # ACCESS TO BLUE PAPER SCREENS FROM DIFFERENT SCREENS
        if current_screen == "room" or current_screen == "paper1" or current_screen == "key1":
            if x > 545 and x < 605 and y > 295 and y < 375:
                current_screen = "bluepaper1"
        if current_screen == "book" or current_screen == "paper2" or current_screen == "key2":
            if x > 545 and x < 605 and y > 295 and y < 375:
                current_screen = "bluepaper2"
        if current_screen == "locked box" or current_screen == "paper3" or current_screen == "key3":
            if x > 545 and x < 605 and y > 295 and y < 375:
                current_screen = "bluepaper3"
        if current_screen == "left side" or current_screen == "paper4" or current_screen == "key4":
            if x > 545 and x < 605 and y > 295 and y < 375:
                current_screen = "bluepaper4"
        if current_screen == "right side" or current_screen == "paper5" or current_screen == "key5":
            if x > 545 and x < 605 and y > 295 and y < 375:
                current_screen = "bluepaper5"

    if key_in_inventory is True:
        # ACCESS TO KEY SCREENS FROM DIFFERENT SCREENS
        if current_screen == "room" or current_screen == "paper1" or current_screen == "pictureframe1" or current_screen == "screwdriver1" or current_screen == "bluepaper1":
            if x > 545 and x < 605 and y > 105 and y < 185:
                current_screen = "key1"
        if current_screen == "book" or current_screen == "paper2" or current_screen == "pictureframe2" or current_screen == "screwdriver2" or current_screen == "bluepaper2":
            if x > 545 and x < 605 and y > 105 and y < 185:
                current_screen = "key2"
        if current_screen == "locked box" or current_screen == "paper3" or current_screen == "pictureframe3" or current_screen == "screwdriver3" or current_screen == "bluepaper3":
            if x > 545 and x < 605 and y > 105 and y < 185:
                current_screen = "key3"
        if current_screen == "left side" or current_screen == "paper4" or current_screen == "pictureframe4" or current_screen == "screwdriver4" or current_screen == "bluepaper4":
            if x > 545 and x < 605 and y > 105 and y < 185:
                current_screen = "key4"
        if current_screen == "right side" or current_screen == "paper5" or current_screen == "pictureframe5" or current_screen == "screwdriver5" or current_screen == "bluepaper5":
            if x > 545 and x < 605 and y > 105 and y < 185:
                current_screen = "key5"

        #BUTTON TO UNLOCK DOOR

        if current_screen == "key1" \
            or current_screen == "key2" \
               or current_screen == "key3" \
               or current_screen == "key4" \
               or current_screen == "key5":
                if x > unlock_button[BTN_X] and x < 400 and y > unlock_button[BTN_Y] and y < 60:
                    current_screen = "victory"
                    game = False


def draw_instruction():
    #DRAW INSTRUCTION SCREEN
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("INSTRUCTIONS", 0, 375, arcade.color.WHITE, 50, WIDTH, "center", "Calibri", True, False)
    arcade.draw_line(40, 360, 600, 360, arcade.color.WHITE, 10)
    arcade.draw_text("In this game, you will be using your wits and brains to try to escape the room", 60, 320, arcade.color.WHITE, font_size=12)
    arcade.draw_text("You will be clicking on different things and trying to use clues to solve puzzles", 60, 290, arcade.color.WHITE, font_size=12 )
    arcade.draw_text("You will only be using your mouse through the entirety of this game", 60, 260, arcade.color.WHITE, font_size=12)
    arcade.draw_text("You can fuse clues together and you can click on them to get more information on it", 60, 230, arcade.color.WHITE, font_size=12)


def draw_mainmenu(x, y):
    #DRAW MAIN MENU
    arcade.set_background_color(arcade.color.GRAY)
    arcade.draw_text("ESCAPE", x, y, arcade.color.RED_DEVIL, 50, 300, "center", "arial", True)
    arcade.draw_text("to the", x + 40, y - 35, arcade.color.BLACK, 25, 200, "center")
    arcade.draw_text("FUTURE", x + 25, y - 90, arcade.color.WHITE, 40, 250, "center", "arial", True)
    arcade.draw_xywh_rectangle_filled(start_button[BTN_X], start_button[BTN_Y], start_button[BTN_WIDTH], start_button[BTN_HEIGHT], arcade.color.LIGHT_GRAY)
    arcade.draw_xywh_rectangle_filled(instructions_button[BTN_X], instructions_button[BTN_Y], instructions_button[BTN_WIDTH], instructions_button[BTN_HEIGHT], arcade.color.LIGHT_GRAY)
    arcade.draw_text("PLAY GAME", 225, 165, arcade.color.BLACK, 25, 900)
    arcade.draw_text("INSTRUCTIONS", 225, 90, arcade.color.BLACK, 19, 900)


def draw_pausescreen():
    #DRAW PAUSE SCREEN
    arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, arcade.color.BLACK)
    arcade.draw_text("QUIT GAME?", 77, HEIGHT / 2, arcade.color.WHITE, 50, 500, "center", "Arial", True)
    arcade.draw_xywh_rectangle_filled(quit_button[BTN_X], quit_button[BTN_Y], quit_button[BTN_WIDTH], quit_button[BTN_HEIGHT], arcade.color.WHITE)
    arcade.draw_xywh_rectangle_filled(resume_button[BTN_X], resume_button[BTN_Y], resume_button[BTN_WIDTH], resume_button[BTN_HEIGHT], arcade.color.WHITE)
    arcade.draw_text("QUIT", 155, 165, arcade.color.BLACK, 25, 300)
    arcade.draw_text("RESUME", 385, 165, arcade.color.BLACK, 25, 500)


def draw_room():
    #DRAW ROOM
    arcade.set_background_color(arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(WIDTH / 2, 40, WIDTH, 80, arcade.color.GRAY)
    arcade.draw_rectangle_filled(260, 155, 75, 150, arcade.color.BROWN)
    arcade.draw_circle_filled(235, 150, 7, arcade.color.GOLD)
    arcade.draw_rectangle_filled(100, 230, 150, 300, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(100, 350, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 290, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 230, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 170, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 110, 125, 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(100, 210, 50, 10, arcade.color.RED)
    arcade.draw_rectangle_filled(410, 165, 125, 10, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(370, 120, 10, 80, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(450, 120, 10, 80, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(410, 185, 60, 30, arcade.color.MAROON)
    arcade.draw_line(380, 185, 440, 185, arcade.color.BLACK)
    arcade.draw_rectangle_filled(410, 185, 5, 10, arcade.color.GOLD)
    draw_arrow_left(58, 40, arcade.color.RED)
    draw_arrow_right(440, 40, arcade.color.RED)


def draw_leftside():
    #DRAW LEFT SIDE
    arcade.set_background_color(arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(WIDTH / 2, 40, WIDTH, 80, arcade.color.GRAY)
    draw_arrow_right(440, 40, arcade.color.RED)
    arcade.draw_rectangle_filled(110, 165, 125, 10, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(70, 120, 10, 80, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(150, 120, 10, 80, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(110, 200, 40, 60, arcade.color.BLACK)
    arcade.draw_rectangle_filled(110, 200, 30, 50, arcade.color.LIGHT_CYAN)


def draw_rightside():
    #DRAW RIGHTSIDE
    arcade.set_background_color(arcade.color.DARK_GRAY)
    arcade.draw_rectangle_filled(WIDTH / 2, 40, WIDTH, 80, arcade.color.GRAY)
    draw_arrow_left(58, 40, arcade.color.RED)
    arcade.draw_rectangle_filled(150, 130, 200, 100, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(150, 185, 40, 10, arcade.color.BLACK)
    arcade.draw_circle_filled(130, 185, 5, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(170, 182, 40, 5, arcade.color.SILVER)


def draw_book():
    #DRAW BOOK
    arcade.draw_rectangle_filled(WIDTH/2 - 70, HEIGHT/2, WIDTH - 145, HEIGHT, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(WIDTH/2 - 70, HEIGHT/2, WIDTH - 145, HEIGHT - 50, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(250, 59, 400, 67, arcade.color.RED)
    arcade.draw_line(50, 59, 12, 40, arcade.color.WHITE, 2)
    draw_arrow_left(70, 435, arcade.color.RED)


def draw_lockedbox():
    #DRAW LOCKED BOX
    arcade.draw_rectangle_filled(WIDTH/2 - 70, 40, WIDTH - 145, 80, arcade.color.LIGHT_BROWN)
    arcade.draw_rectangle_filled(WIDTH/2 - 70, 170, 360, 180, arcade.color.MAROON)
    arcade.draw_line(70, 170, 430, 170, arcade.color.BLACK)
    arcade.draw_rectangle_filled(WIDTH/2 - 70, 170, 30, 60, arcade.color.GOLD)
    arcade.draw_rectangle_filled(150, 215, 40, 40, arcade.color.GRAY)
    arcade.draw_rectangle_filled(350, 215, 40, 40, arcade.color.GRAY)
    arcade.draw_rectangle_filled(150, 125, 40, 40, arcade.color.GRAY)
    arcade.draw_rectangle_filled(350, 125, 40, 40, arcade.color.GRAY)
    arcade.draw_triangle_filled(150, 255, 130, 240, 170, 240, arcade.color.GRAY)
    arcade.draw_triangle_filled(150, 175, 130, 190, 170, 190, arcade.color.GRAY)
    arcade.draw_triangle_filled(350, 255, 330, 240, 370, 240, arcade.color.GRAY)
    arcade.draw_triangle_filled(350, 175, 330, 190, 370, 190, arcade.color.GRAY)
    arcade.draw_triangle_filled(150, 165, 130, 150, 170, 150, arcade.color.GRAY)
    arcade.draw_triangle_filled(150, 85, 130, 100, 170, 100, arcade.color.GRAY)
    arcade.draw_triangle_filled(350, 165, 330, 150, 370, 150, arcade.color.GRAY)
    arcade.draw_triangle_filled(350, 85, 330, 100, 370, 100, arcade.color.GRAY)
    arcade.draw_text(f"{player_input1}", 137, 195, arcade.color.BLACK, 40)
    arcade.draw_text(f"{player_input2}", 337, 195, arcade.color.BLACK, 40)
    arcade.draw_text(f"{player_input3}", 137, 105, arcade.color.BLACK, 40)
    arcade.draw_text(f"{player_input4}", 337, 105, arcade.color.BLACK, 40)
    draw_arrow_left(70, 435, arcade.color.RED)


def draw_sidebar(whitesquare_y):
    #DRAW SIDEBAR AND COVER UP ITEMS ALREADY TAKEN
    arcade.draw_rectangle_filled(570, HEIGHT / 2, 145, HEIGHT, arcade.color.BLACK)
    for _ in range(5):
        arcade.draw_rectangle_filled(570, whitesquare_y, 80, 80, arcade.color.WHITE)
        whitesquare_y -= 95
    if paper_in_inventory is True:
        arcade.draw_rectangle_filled(570, 430, 50, 70, arcade.color.BEIGE)
    if paper_in_inventory is True and current_screen == "book":
        arcade.draw_xywh_rectangle_filled(12, 39, 38, 21, arcade.color.DARK_BROWN)
    if pictureframe_in_inventory is True:
        arcade.draw_rectangle_filled(570, 335, 40, 60, arcade.color.BLACK)
        arcade.draw_rectangle_filled(570, 335, 30, 50, arcade.color.LIGHT_CYAN)
    if pictureframe_in_inventory is True and current_screen == "left side":
        arcade.draw_rectangle_filled(110, 200, 40, 60, arcade.color.DARK_GRAY)
    if screwdriver_in_inventory is True:
        arcade.draw_rectangle_filled(560, 230, 40, 10, arcade.color.BLACK, 45)
        arcade.draw_circle_filled(545, 215, 5, arcade.color.BLACK,)
        arcade.draw_rectangle_filled(588, 258, 40, 5, arcade.color.SILVER, 45)
    if screwdriver_in_inventory is True and current_screen == "right side":
        arcade.draw_xywh_rectangle_filled(125, 180, 186, 20, arcade.color.DARK_GRAY)
    if bluepaper_in_inventory is True:
        arcade.draw_rectangle_filled(570, 335, 60, 60, arcade.color.LIGHT_BLUE)
    if bluepaper_in_inventory is True and current_screen == "left side":
        arcade.draw_rectangle_filled(110, 200, 40, 60, arcade.color.DARK_GRAY)
    if bluepaper_in_inventory is True and current_screen == "right side":
        arcade.draw_xywh_rectangle_filled(125, 180, 186, 20, arcade.color.DARK_GRAY)
    if key_in_inventory is True:
        arcade.draw_circle_filled(550, 125, 15, arcade.color.GOLD)
        arcade.draw_circle_filled(550, 125, 8, arcade.color.WHITE)
        arcade.draw_rectangle_filled(575, 150, 50, 8, arcade.color.GOLD, 45)
        arcade.draw_rectangle_filled(580, 145, 20, 8, arcade.color.GOLD, -45)
        arcade.draw_rectangle_filled(590, 155, 20, 8, arcade.color.GOLD, -45)


def draw_paper():
    #DRAW PAPER
    arcade.draw_rectangle_filled(WIDTH/2 - 70, HEIGHT/2, WIDTH - 145, HEIGHT, arcade.color.WHITE)
    arcade.draw_rectangle_filled(WIDTH/2 - 70, HEIGHT/2, 267, 373, arcade.color.BEIGE)
    arcade.draw_text("LOST", 200, 200, arcade.color.BLACK, 25, 500, "left", 'arial', False, False, "left",
                     "baseline", 50)
    draw_arrow_left(70, 435, arcade.color.BLACK)


def draw_pictureframe():
    #DRAW PICTURE FRAME
    arcade.draw_rectangle_filled(WIDTH / 2 - 70, HEIGHT / 2, WIDTH - 145, HEIGHT, arcade.color.WHITE)
    arcade.draw_rectangle_filled(WIDTH / 2 - 70, HEIGHT / 2, 213, 320, arcade.color.BLACK)
    arcade.draw_rectangle_filled(WIDTH / 2 - 70, HEIGHT / 2, 160, 267, arcade.color.LIGHT_CYAN)
    draw_arrow_left(70, 435, arcade.color.BLACK)
    if pictureframe_in_inventory and screwdriver_in_inventory:
        arcade.draw_xywh_rectangle_filled(fuse_button[BTN_X], fuse_button[BTN_Y], fuse_button[BTN_X] + fuse_button[BTN_WIDTH], fuse_button[BTN_Y] + fuse_button[BTN_HEIGHT], arcade.color.GRAY)
        arcade.draw_text("FUSE WITH SCREWDRIVER", fuse_button[BTN_X] + 15, fuse_button[BTN_Y] + 5, arcade.color.BLACK, 20)


def draw_screwdriver():
    #DRAW SCREWDRIVER
    arcade.draw_rectangle_filled(WIDTH / 2 - 70, HEIGHT / 2, WIDTH - 145, HEIGHT, arcade.color.WHITE)
    arcade.draw_rectangle_filled(170, 170, 213, 53, arcade.color.BLACK, 45)
    arcade.draw_circle_filled(100, 99, 27, arcade.color.BLACK)
    arcade.draw_rectangle_filled(320, 320, 213, 27, arcade.color.SILVER, 45)
    draw_arrow_left(70, 435, arcade.color.BLACK)
    if pictureframe_in_inventory and screwdriver_in_inventory:
        arcade.draw_xywh_rectangle_filled(fuse_button[BTN_X], fuse_button[BTN_Y], fuse_button[BTN_X] + fuse_button[BTN_WIDTH], fuse_button[BTN_Y] + fuse_button[BTN_HEIGHT], arcade.color.GRAY)
        arcade.draw_text("FUSE WITH PICTURE FRAME", fuse_button[BTN_X] + 9, fuse_button[BTN_Y] + 5, arcade.color.BLACK, 20)


def draw_bluepaper():
    #DRAW SCREWDRIVER
    arcade.draw_rectangle_filled(WIDTH / 2 - 70, HEIGHT / 2, WIDTH - 145, HEIGHT, arcade.color.WHITE)
    arcade.draw_rectangle_filled(WIDTH / 2 - 70, HEIGHT / 2, 300, 300, arcade.color.LIGHT_BLUE)
    arcade.draw_text("O=1, L=4, T=3, S=2", 110, HEIGHT / 2, arcade.color.BLACK, 30)
    draw_arrow_left(70, 435, arcade.color.BLACK)


def draw_key(x):
    #DRAW KEY
    arcade.draw_rectangle_filled(WIDTH / 2 - 70, HEIGHT / 2, WIDTH - 145, HEIGHT, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 50, 150, 60, arcade.color.GOLD)
    arcade.draw_circle_filled(x + 50, 150, 32, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x + 150, 250, 200, 32, arcade.color.GOLD, 45)
    arcade.draw_rectangle_filled(x + 175, 230, 80, 32, arcade.color.GOLD, -45)
    arcade.draw_rectangle_filled(x + 210, 270, 80, 32, arcade.color.GOLD, -45)
    arcade.draw_xywh_rectangle_filled(unlock_button[BTN_X], unlock_button[BTN_Y],
                                      unlock_button[BTN_X] + unlock_button[BTN_WIDTH],
                                      unlock_button[BTN_Y] + unlock_button[BTN_HEIGHT], arcade.color.GRAY)
    arcade.draw_text("UNLOCK DOOR", unlock_button[BTN_X] + 70, unlock_button[BTN_Y] + 5, arcade.color.BLACK, 20)
    draw_arrow_left(70, 435, arcade.color.BLACK)


def draw_victory():
    #DRAW VICTORY SCREEN
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_text("CONGRATULATIONS!", 50, HEIGHT / 2, arcade.color.WHITE, 50)
    arcade.draw_text("YOU UNLOCKED THE DOOR WITH THE KEY AND ESCAPED!", 100, HEIGHT / 2 - 25, arcade.color.WHITE, 15)
    arcade.draw_text("Press ESC to go back to the main menu", 200, HEIGHT/ 2 - 50, arcade.color.WHITE, 10)


def draw_arrow_left(x, y, color):
    #DRAW ARROW POINTING LEFT
    arcade.draw_rectangle_filled(x, y, 70, 30, color)
    arcade.draw_triangle_filled(x - 55, y, x - 10, y + 35, x - 10, y - 35, color)


def draw_arrow_right(x, y, color):
    #DRAW ARROW POINTING RIGHT
    arcade.draw_rectangle_filled(x, y, 70, 30, color)
    arcade.draw_triangle_filled(x + 55, y, x + 10, y + 35, x + 10, y - 35, color)


if __name__ == '__main__':
    setup()
