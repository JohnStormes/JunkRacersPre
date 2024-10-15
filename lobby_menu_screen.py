# Johnathan Stormes

import pygame
import helper
from visualcomponents import button

# general vars
create = False
join = False
join_enter = False
back = False
cover = False
cur_letter = 0
code = []

# button vars
create_img = -1
create_img_pressed = -1
create_button = -1

join_img = -1
join_img_pressed = -1
join_button = -1

back_img = -1
back_img_pressed = -1
back_button = -1

join_enter_img = -1
join_enter_img_pressed = -1
join_enter_button = -1

# misc images
cover_img = -1
join_img = -1
join_rect = -1

# initialization. Vars must be initialized here or else they would be initialized before pygame window is created
def __init__():
    global create_img, create_img_pressed, create_button, join_img, join_img_pressed, join_button
    global back_img, back_img_pressed, back_button, cover_img, join_img, join_rect
    global join_enter_img, join_enter_img_pressed, join_enter_button

    create_img = pygame.image.load("images/button_images/create_button.png").convert_alpha()
    create_img_pressed = pygame.image.load("images/button_images/create_button_pressed.png").convert_alpha()
    create_button = button.Button(250, 350, create_img, create_img_pressed, 480, 200)

    join_img = pygame.image.load("images/button_images/join_button.png").convert_alpha()
    join_img_pressed = pygame.image.load("images/button_images/join_button_pressed.png").convert_alpha()
    join_button = button.Button(870, 350, join_img, join_img_pressed, 480, 200)

    back_img = pygame.image.load("images/button_images/back_button.png").convert_alpha()
    back_img_pressed = pygame.image.load("images/button_images/back_button_pressed.png").convert_alpha()
    back_button = button.Button(0, 0, back_img, back_img_pressed, 200, 200)

    join_enter_img = pygame.image.load("images/button_images/join_enter_button.png").convert_alpha()
    join_enter_img_pressed = pygame.image.load("images/button_images/join_enter_button_pressed.png").convert_alpha()
    join_enter_button = button.Button(1050, 460, join_enter_img, join_enter_img_pressed, 150, 150)

    cover_img = pygame.image.load("images/black_cover.jpg").convert_alpha()
    cover_img.set_alpha(150)
    cover_img = pygame.transform.scale(cover_img, (helper.CLIENT_SCREEN_WIDTH, helper.CLIENT_SCREEN_HEIGHT))

    join_img = pygame.image.load("images/join.png").convert_alpha()
    join_img = pygame.transform.scale(join_img, (helper.getScreenX(1100), helper.getScreenY(500)))
    join_rect = join_img.get_rect()
    join_rect.topleft = (helper.getScreenX(250), helper.getScreenY(200))

# draws for when the main screen is open
def drawMain(window):
    create_button.draw(window)
    join_button.draw(window)
    back_button.draw(window)

# draws for when the join prompt is open
def drawJoin(window):
    window.blit(cover_img, (0, 0))
    window.blit(join_img, (join_rect.x, join_rect.y))
    helper.drawText(window, "enter join code:", helper.getArialFont(150), (0, 0, 0), helper.getScreenX(480), helper.getScreenY(270))
    join_enter_button.draw(window)
    for x in range(len(code)):
        helper.drawText(window, code[x], helper.getArialFont(helper.getScreenX(140)), (0, 0, 0),
                        helper.getScreenX(410 + x * 122), helper.getScreenY(460))

# all draws for title screen state
def draw(window):
    drawMain(window)
    if join:
        drawJoin(window)

# update calls for when the main screen is open
def updateMain():
    global create, join, back, cover
    # update the buttons
    create_button.update()
    join_button.update()
    back_button.update()

    # do button actions on release. Can be changed to on click
    if create_button.click_release:
        print("create")
        # add screen for settings in lobby creation
        create = True
        create_button.click_release = False
    elif join_button.click_release:
        print("join")
        cover = True
        join = True
        join_button.click_release = False
    elif back_button.click_release:
        print("back")
        back = True
        back_button.click_release = False

# update calls for when the join dialogue is open
def updateJoin():
    global join_rect, join, join_enter, code, join_img, join_rect

    # update button
    join_enter_button.update()

    # get mouse position
    pos = pygame.mouse.get_pos()

    # check if mouse outside of window
    if not join_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            join = False

    # do button action on release
    if join_enter_button.click_release:
        print("join enter")
        join_enter = True
        join_enter_button.click_release = False

    join_img = pygame.transform.scale(join_img, (helper.getScreenX(1100), helper.getScreenY(500)))
    join_rect = join_img.get_rect()
    join_rect.topleft = (helper.getScreenX(250), helper.getScreenY(200))

# join code manipulation
def addToCode(letter):
    global code
    if len(code) < 5:
        code.append(pygame.key.name(letter).upper())
def codeBackspace():
    global code
    code = code[:-1]

# all updates for lobby menu screen state
def update():
    global join, create
    if not join and not create:
        updateMain()
    elif join:
        updateJoin()
    elif create:
        pass