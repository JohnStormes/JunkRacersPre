# Johnathan Stormes

import pygame
from network import Network
from player import Player
import sys
import title_screen
import lobby_menu_screen
import settings_screen
import helper
from visualcomponents import button

# window setup
CLIENT_SCREEN_WIDTH = helper.CLIENT_SCREEN_WIDTH
CLIENT_SCREEN_HEIGHT = helper.CLIENT_SCREEN_HEIGHT
SCREEN_WIDTH = helper.SCREEN_WIDTH
SCREEN_HEIGHT = helper.SCREEN_HEIGHT
# fullscreen resizable
window = pygame.display.set_mode(((CLIENT_SCREEN_WIDTH - 10, CLIENT_SCREEN_HEIGHT - 50)), pygame.RESIZABLE)
# fullscreen fill
# window = pygame.display.set_mode(((0, 0)), pygame.FULLSCREEN)
# 500x500 resizable
#window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Junk Racers (pre)")

# client side vars
screen = 0
TITLE_SCREEN = 0
SETTINGS_SCREEN = 1
LOBBY_MENU_SCREEN = 2
LOBBY_SCREEN = 3
num_players = 0

# inits
title_screen.__init__()
lobby_menu_screen.__init__()
settings_screen.__init__()

# called when a client attempts to join a lobby
def attemptJoin(join_code):
    print(join_code)

# ______________________________________________________________________________________________________
# this client's update function. ALL UPDATE FROM HERE
def update(window, client_player, players):
    global screen
    if screen == 0:
        title_screen.update()
        if title_screen.play:
            screen = 2
            title_screen.play = False
        elif title_screen.settings:
            screen = 1
            title_screen.settings = False
    elif screen == 1:
        settings_screen.update()
        if settings_screen.back:
            screen = 0
            settings_screen.back = False
    elif screen == 2:
        lobby_menu_screen.update()
        if lobby_menu_screen.back:
            screen = 0
            lobby_menu_screen.back = False
        if lobby_menu_screen.join_enter:
            attemptJoin(lobby_menu_screen.code)
            lobby_menu_screen.code = []
            lobby_menu_screen.join_enter = False
            lobby_menu_screen.join = False
    helper.update()

# ______________________________________________________________________________________________________
# this client's draw function. ALL DRAW FROM HERE
def draw(window, client_player, players):
    global num_players
    if screen == 0:
        title_screen.draw(window, client_player, players)
    elif screen == 1:
        settings_screen.draw(window)
    elif screen == 2:
        lobby_menu_screen.draw(window)


# this clients network init and game loop, handles network and player data being received from server
def main():
    global num_players
    run = True
    n = Network()
    p = n.getData()

    clock = pygame.time.Clock()

    # game loop for this client
    while run:
        #frame rate
        clock.tick(60)
        # send p data to network, receive p2 data from network. Network interacts with server for this data
        data = n.send(p)
        num_players = data[1]

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # code typing in lobby menu screen
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    lobby_menu_screen.addToCode(event.key)
                elif event.key == pygame.K_BACKSPACE:
                    lobby_menu_screen.codeBackspace()
        if screen == 0 and title_screen.quit:
            run = False
            pygame.quit()
            break

        # UPDATE CALLS
        update(window, p, data[0])

        window.fill((255, 255, 255))

        # DRAW CALLS
        draw(window, p, data[0])

        pygame.display.update()

main()
sys.exit()