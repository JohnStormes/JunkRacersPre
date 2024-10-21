# Johnathan Stormes
import pygame
import helper
from visualcomponents import button

# general vars
exit = False

exit_img = -1
exit_img_pressed = -1
exit_button = -1

background_img = -1

# initialize buttons, images, etc
def __init__():
    global exit_img, exit_img_pressed, exit_button, background_img

    exit_img = pygame.image.load("images/button_images/exit_button.png").convert_alpha()
    exit_img_pressed = pygame.image.load("images/button_images/exit_button_pressed.png").convert_alpha()
    exit_button = button.Button(0, 0, exit_img, exit_img_pressed, 240, 100)

    background_img = pygame.image.load("images/lobby_background.png").convert_alpha()
    background_img = pygame.transform.scale(background_img, (helper.CLIENT_SCREEN_WIDTH, helper.CLIENT_SCREEN_HEIGHT))


# all draw calls for lobby screen
def draw(window, player, players, host_id, team_list):
    # make sure server and client data are synced
    # host_id and team_list should never be -1 because this would indicate the client is not in a lobby,
    # but this draw call can only be occuring if the client screen is set to be in a lobby
    if host_id == -1 or team_list == -1:
        print("client is displaying lobby but server is not sending lobby specific information")
        return
    
    # background draw calls
    window.blit(background_img, (0, 0))
    
    # button draw calls
    exit_button.draw(window)

    # text draw calls
    helper.drawText(window, player.lobbyID, helper.getArialFont(helper.getScreenX(150)), (0, 0, 0),
                    helper.getScreenX(50), helper.getScreenY(700))
    helper.drawText(window, "players in lobby: " + str(len(players)), helper.getArialFont(helper.getScreenX(50)), (0, 0, 0),
                    helper.getScreenX(300), helper.getScreenY(50))
    
    # temp draw functions of players in lobby
    for x in range(len(players)):
        if players[x].ID != player.ID:
            players[x].draw(window, host_id, False, team_list)
    player.move()
    player.draw(window, host_id, True, team_list)

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