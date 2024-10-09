# Johnathan Stormes

import pygame
from Network import Network
from Player import Player
import os
import TitleScreen
import Helper

# window setup
CLIENT_SCREEN_WIDTH = Helper.getClientScreenWidth()
CLIENT_SCREEN_HEIGHT = Helper.getClientScreenHeight()
SCREEN_WIDTH = Helper.getScreenWidth()
SCREEN_HEIGHT = Helper.getScreenHeight()
#window = pygame.display.set_mode((CLIENT_SCREEN_WIDTH - 10, CLIENT_SCREEN_HEIGHT - 50), pygame.RESIZABLE)
window = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
pygame.display.set_caption("Junk Racers (pre)")

# client side vars
screen = 0
TITLE_SCREEN = 0
SETTINGS_SCREEN = 1
LOBBY_MENU_SCREEN = 2
LOBBY_SCREEN = 3
num_players = 0

# get a resized location value for this clients screen size
def getScreenX(x):
    newx = float(x) / float(SCREEN_WIDTH) * float(CLIENT_SCREEN_WIDTH)
    return int(newx)
def getScreenY(y):
    newy = float(y) / float(SCREEN_HEIGHT) * float(CLIENT_SCREEN_HEIGHT)
    return int(newy)

# this client's draw function. ALL DRAW FROM HERE
def redrawWindow(window, client_player, players):
    global num_players
    window.fill((0, 0, 0))
    TitleScreen.draw(window, num_players, client_player.getID())
    if (players[0].getID() != client_player.getID()):
        for x in range (len(players)):
            players[x].draw(window)
    client_player.draw(window)
    pygame.display.update()

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
        p.move()
        redrawWindow(window, p, data[0])

main()