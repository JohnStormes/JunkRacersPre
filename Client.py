# Johnathan Stormes

import pygame
from network import Network
from player import Player
import sys
import title_screen
import lobby_menu_screen
import settings_screen
import lobby_screen
import helper
from visualcomponents import button
from lobby import Lobby

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
decision = helper.NO_DECISION
join_code_attempt = ""

# inits
title_screen.__init__()
lobby_menu_screen.__init__()
settings_screen.__init__()
lobby_screen.__init__()

# called when a client attempts to join a lobby
def attemptJoin(join_code):
    global decision, join_code_attempt
    print(join_code)
    decision = helper.JOIN_LOBBY
    for x in range(5):
        join_code_attempt += join_code[x]

# called when a client attempts to create a lobby
def createLobby():
    global decision
    decision = helper.CREATE_LOBBY

# ______________________________________________________________________________________________________
# this client's update function. ALL UPDATE FROM HERE
def update(window, client_player, players):
    global screen, decision
    # title screen update and client button actions
    if screen == TITLE_SCREEN:
        title_screen.update()
        if title_screen.play:
            screen = LOBBY_MENU_SCREEN
            title_screen.play = False
        elif title_screen.settings:
            screen = SETTINGS_SCREEN
            title_screen.settings = False

    # settings screen update and client button actions
    elif screen == SETTINGS_SCREEN:
        settings_screen.update()
        if settings_screen.back:
            screen = TITLE_SCREEN
            settings_screen.back = False

    # lobby menu screen update and client button actions
    elif screen == LOBBY_MENU_SCREEN:
        lobby_menu_screen.update()
        if lobby_menu_screen.back:
            screen = TITLE_SCREEN
            lobby_menu_screen.back = False
        elif lobby_menu_screen.create:
            screen = LOBBY_SCREEN
            createLobby()
            lobby_menu_screen.create = False
        elif lobby_menu_screen.join_enter:
            attemptJoin(lobby_menu_screen.code)
            lobby_menu_screen.code = []
            lobby_menu_screen.join_enter = False
            lobby_menu_screen.join = False

    # lobby screen update and client button actions
    elif screen == LOBBY_SCREEN:
        lobby_screen.update()
        if lobby_screen.exit:
            screen = LOBBY_MENU_SCREEN
            decision = helper.LEAVE_LOBBY
            lobby_screen.exit = False
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
    elif screen == 3:
        lobby_screen.draw(window, client_player, players)


# this clients network init and game loop, handles network and player data being received from server
def main():
    global num_players, decision, join_code_attempt, screen
    run = True
    n = Network()
    p = n.getData()

    clock = pygame.time.Clock()

    # game loop for this client
    while run:
        #frame rate
        clock.tick(60)
        # send data to network to send to server, and receive server side data back
        # sending out:
        # data[0]: this client's player
        # data[1]: decision for player action in lobby
        # data[2]: join code attempt if and only if decision = helper.JOIN_LOBBY
        data = n.send((p, decision, join_code_attempt))

        # find this client in player list and update player object
        for x in range(len(data[0])):
            if data[0][x].getID() == p.getID():
                p = data[0][x]

        # check if player joined lobby
        if join_code_attempt != "" and p.lobbyID != "":
            screen = LOBBY_SCREEN

        # ensure that a decision/join code is sent to the server ONLY ONCE
        if decision != helper.NO_DECISION:
            decision = helper.NO_DECISION
        if join_code_attempt != "":
            join_code_attempt = ""

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