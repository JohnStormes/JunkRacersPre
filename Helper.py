# Johnathan Stormes
import pygame
import os

# client <-> server data transfer constants
NO_DECISION = 0
CREATE_LOBBY = 1
JOIN_LOBBY = 2
LEAVE_LOBBY = 3

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()
CLIENT_SCREEN_WIDTH, CLIENT_SCREEN_HEIGHT = info.current_w, info.current_h

# screen width and height used for all drawings, converted into client width and height for display
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# GET SCREEN LOCATIONS FOR ALL SIZINGS AND POSITIONS
def getScreenX(x):
    newx = float(x) / float(SCREEN_WIDTH) * float(CLIENT_SCREEN_WIDTH)
    return int(newx)
def getScreenY(y):
    newy = float(y) / float(SCREEN_HEIGHT) * float(CLIENT_SCREEN_HEIGHT)
    return int(newy)

# visuals
def drawText(window, text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x, y))

# fonts / text
def getArialFont(size):
    return pygame.font.SysFont("Arial", size)

# update window size
def update():
    global CLIENT_SCREEN_WIDTH, CLIENT_SCREEN_HEIGHT
    info = pygame.display.Info()
    CLIENT_SCREEN_WIDTH, CLIENT_SCREEN_HEIGHT = info.current_w, info.current_h
