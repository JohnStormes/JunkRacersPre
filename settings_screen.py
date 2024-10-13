# Johnathan Stormes

import pygame
import helper
from visualcomponents import button

# general vars
back = False

# button vars
back_img = -1
back_img_pressed = -1
back_button = -1

# initialization. Vars must be initialized here or else they would be initialized before pygame window is created
def __init__():
    global back_img, back_img_pressed, back_button

    back_img = pygame.image.load("images/button_images/back_button.png").convert_alpha()
    back_img_pressed = pygame.image.load("images/button_images/back_button_pressed.png").convert_alpha()

    back_button = button.Button(0, 0, back_img, back_img_pressed, 200, 200)


# all draws for title screen state
def draw(window):
    back_button.draw(window)


# all updates for title screen state
def update():
    global create, join, back
    # update the buttons
    back_button.update()

    # do button actions on release. Can be changed to on click
    if back_button.click_release:
        print("back")
        back = True
        back_button.click_release = False