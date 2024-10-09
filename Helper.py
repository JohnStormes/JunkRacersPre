# Johnathan Stormes
import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()
CLIENT_SCREEN_WIDTH, CLIENT_SCREEN_HEIGHT = info.current_w, info.current_h

# screen width and height used for all drawings, converted into client width and height for display
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

class Helper:
    
    # get a resized location value for this clients screen size
    @staticmethod
    def getScreenX(x):
        newx = float(x) / float(SCREEN_WIDTH) * float(CLIENT_SCREEN_WIDTH)
        return int(newx)
    @staticmethod
    def getScreenY(y):
        newy = float(y) / float(SCREEN_HEIGHT) * float(CLIENT_SCREEN_HEIGHT)
        return int(newy)
    
    # get general screen values
    @staticmethod
    def getClientScreenWidth():
        return CLIENT_SCREEN_WIDTH
    @staticmethod
    def getClientScreenHeight():
        return CLIENT_SCREEN_HEIGHT
    @staticmethod
    def getScreenHeight():
        return SCREEN_HEIGHT
    @staticmethod
    def getScreenWidth():
        return SCREEN_WIDTH