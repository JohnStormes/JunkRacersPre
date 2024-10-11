# Johnathan Stormes

import pygame
from network import Network
from player import Player
import os
import title_screen
import helper

# window setup
CLIENT_SCREEN_WIDTH = helper.getClientScreenWidth()
CLIENT_SCREEN_HEIGHT = helper.getClientScreenHeight()
SCREEN_WIDTH = helper.getScreenWidth()
SCREEN_HEIGHT = helper.getScreenHeight()
# fullscreen
window = pygame.display.set_mode(((CLIENT_SCREEN_WIDTH - 10, CLIENT_SCREEN_HEIGHT - 50)), pygame.RESIZABLE)
# 500x500
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

# ______________________________________________________________________________________________________
# this client's update function. ALL UPDATE FROM HERE
def update(window, client_player, players):
    title_screen.update()
    helper.update()

# ______________________________________________________________________________________________________
# this client's draw function. ALL DRAW FROM HERE
def draw(window, client_player, players):
    global num_players
    title_screen.draw(window, num_players, client_player.getID())

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

        # UPDATE CALLS
        update(window, p, data[0])

        window.fill((255, 255, 255))

        # DRAW CALLS
        draw(window, p, data[0])

        pygame.display.update()

main()