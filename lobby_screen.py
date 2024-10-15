# Johnathan Stormes
import pygame
import helper
from visualcomponents import button

# general vars
exit = False

exit_img = -1
exit_img_pressed = -1
exit_button = -1

# initialize buttons, images, etc
def __init__():
    global exit_img, exit_img_pressed, exit_button

    exit_img = pygame.image.load("images/button_images/exit_button.png").convert_alpha()
    exit_img_pressed = pygame.image.load("images/button_images/exit_button_pressed.png").convert_alpha()
    exit_button = button.Button(0, 0, exit_img, exit_img_pressed, 240, 100)


# all draw calls for lobby screen
def draw(window, player, players):
    # button draw calls
    exit_button.draw(window)
    helper.drawText(window, player.lobbyID, helper.getArialFont(helper.getScreenX(150)), (0, 0, 0),
                    helper.getScreenX(50), helper.getScreenY(700))
    helper.drawText(window, "players in lobby: " + str(len(players)), helper.getArialFont(helper.getScreenX(50)), (0, 0, 0),
                    helper.getScreenX(300), helper.getScreenY(50))
    
    # temp draw functions of players in lobby
    for x in range(len(players)):
        if players[x].ID != player.ID:
            players[x].draw(window)
    player.move()
    player.draw(window)

# all updates for lobby screen
def update():
    global exit
    # update buttons
    exit_button.update()

    # do button actions on release
    if exit_button.click_release:
        print("exit lobby")
        exit = True
        exit_button.click_release = False