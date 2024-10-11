# Johnathan Stormes
import pygame
import helper
from visualcomponents import button

# arial font
text_font = pygame.font.SysFont("Arial", 30)

# button vars
start_img = -1
settings_img = -1
start_button = -1
settings_button = -1
play_button_pressed = False
settings_button_pressed = False

def __init__():
    global start_img, settings_img, start_button, settings_button
    start_img = pygame.image.load("images/button_images/start_button.png").convert_alpha()
    settings_img = pygame.image.load("images/button_images/settings_button.png").convert_alpha()
    start_button = button.Button(600, 200, start_img, 400, 200)
    settings_button = button.Button(560, 500, settings_img, 480, 200)

def draw(window, num_players, player_id):
    #Helper.drawText(window, "players: " + str(num_players), text_font, (255, 255, 255), 220, 250)
    #Helper.drawText(window, "ID: " + str(player_id), text_font, (255, 255, 255), 400, 10)
    start_button.draw(window)
    settings_button.draw(window)

def update():
    start_button.update()
    settings_button.update()
    if start_button.clicked:
        print("start")
    if settings_button.clicked:
        print("settings")