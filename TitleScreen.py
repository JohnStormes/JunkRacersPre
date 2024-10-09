# Johnathan Stormes
import pygame
from Helper import Helper

def draw(window):
    pygame.draw.rect(window, (255, 255, 255), (0, 0, Helper.getScreenX(800), Helper.getScreenY(450)))

def update():
    pass