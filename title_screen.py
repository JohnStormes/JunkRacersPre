# Johnathan Stormes
import pygame
import helper
from visualcomponents import button

# general vars
quit = False
play = False
settings = False

# button vars
start_img = -1
start_img_pressed = -1
start_button = -1

settings_img = -1
settings_img_pressed = -1
settings_button = -1

exit_img = -1
exit_img_pressed = -1
exit_button = -1

# initialization. Vars must be initialized here or else they would be initialized before pygame window is created
def __init__():
    global start_img, settings_img, start_button, settings_button, exit_img, exit_button
    global start_img_pressed, settings_img_pressed, exit_img_pressed

    start_img = pygame.image.load("images/button_images/start_button.png").convert_alpha()
    start_img_pressed = pygame.image.load("images/button_images/start_button_pressed.png").convert_alpha()

    settings_img = pygame.image.load("images/button_images/settings_button.png").convert_alpha()
    settings_img_pressed = pygame.image.load("images/button_images/settings_button_pressed.png").convert_alpha()

    exit_img = pygame.image.load("images/button_images/exit_button.png").convert_alpha()
    exit_img_pressed = pygame.image.load("images/button_images/exit_button_pressed.png").convert_alpha()

    start_button = button.Button(560, 100, start_img, start_img_pressed, 480, 200)
    settings_button = button.Button(560, 350, settings_img, settings_img_pressed, 480, 200)
    exit_button = button.Button(560, 600, exit_img, exit_img_pressed, 480, 200)


# all draws for title screen state
def draw(window, client_player, players):
    # debugging display for number of players and player ID
    if client_player.getID() == players[0].getID():
        num_players = 1
    else:
        num_players = len(players) + 1
    player_id = client_player.getID()
    helper.drawText(window, "players: " + str(num_players), helper.getArialFont(30), (0, 0, 0), 220, 250)
    helper.drawText(window, "ID: " + str(player_id), helper.getArialFont(30), (0, 0, 0), 400, 10)

    # button draw calls
    start_button.draw(window)
    settings_button.draw(window)
    exit_button.draw(window)


# all updates for title screen state
def update():
    global quit, play, settings
    # update the buttons
    start_button.update()
    settings_button.update()
    exit_button.update()

    # do button actions on release. Can be changed to on click
    if start_button.click_release:
        print("start")
        play = True
        start_button.click_release = False
    elif settings_button.click_release:
        print("settings")
        settings = True
        settings_button.click_release = False
    elif exit_button.click_release:
        print("exit")
        quit = True
        exit_button.click_release = False