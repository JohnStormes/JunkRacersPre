# Johnathan Stormes
import pygame
import Helper

# arial font
text_font = pygame.font.SysFont("Arial", 30)

def draw(window, num_players, player_id):
    #pygame.draw.rect(window, (255, 255, 255), (0, 0, Helper.getScreenX(800), Helper.getScreenY(450)))
    Helper.drawText(window, "players: " + str(num_players), text_font, (255, 255, 255), 220, 250)
    Helper.drawText(window, "ID: " + str(player_id), text_font, (255, 255, 255), 400, 10)
def update():
    pass