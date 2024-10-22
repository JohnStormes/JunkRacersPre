# Johnathan Stormes
import pygame
import helper
from visualcomponents import button

# general vars
exit = False
change_team = False
change_team_value = -1

exit_img = -1
exit_img_pressed = -1
exit_button = -1

join_team_img = -1
join_team_img_pressed = -1
join_team_buttons = -1

background_img = -1

garage_door_img = -1

garage_1_on = -1
garage_2_on = -1
garage_3_on = -1
garage_4_on = -1
garage_5_on = -1

# initialize buttons, images, etc
def __init__():
    global exit_img, exit_img_pressed, exit_button, background_img, garage_door_img
    global join_team_img, join_team_img_pressed, join_team_buttons
    global garage_1_on, garage_2_on, garage_3_on, garage_4_on, garage_5_on

    exit_img = pygame.image.load("images/button_images/exit_button.png").convert_alpha()
    exit_img_pressed = pygame.image.load("images/button_images/exit_button_pressed.png").convert_alpha()
    exit_button = button.Button(0, 0, exit_img, exit_img_pressed, 240, 100)

    background_img = pygame.image.load("images/lobby_background.png").convert_alpha()
    background_img = pygame.transform.scale(background_img, (helper.CLIENT_SCREEN_WIDTH, helper.CLIENT_SCREEN_HEIGHT))

    garage_door_img = pygame.image.load("images/garage_door.png").convert_alpha()
    garage_door_img = pygame.transform.scale(garage_door_img, (helper.getScreenX(300), helper.getScreenY(165)))

    join_team_img = pygame.image.load("images/button_images/join_team_button.png").convert_alpha()
    join_team_img_pressed = pygame.image.load("images/button_images/join_team_button_pressed.png").convert_alpha()
    join_team_buttons = []
    for x in range(5):
        join_team_buttons.append(button.Button(92 + x * 320, 270, join_team_img, join_team_img_pressed, 140, 50))

    garage_1_on = pygame.image.load("images/garage_1_on.png").convert_alpha()
    garage_1_on = pygame.transform.scale(garage_1_on, (garage_1_on.get_width() * 0.26, garage_1_on.get_height() * 0.26))
    garage_2_on = pygame.image.load("images/garage_2_on.png").convert_alpha()
    garage_2_on = pygame.transform.scale(garage_2_on, (garage_2_on.get_width() * 0.26, garage_2_on.get_height() * 0.26))
    garage_3_on = pygame.image.load("images/garage_3_on.png").convert_alpha()
    garage_3_on = pygame.transform.scale(garage_3_on, (garage_3_on.get_width() * 0.016, garage_3_on.get_height() * 0.016))
    garage_4_on = pygame.image.load("images/garage_4_on.png").convert_alpha()
    garage_4_on = pygame.transform.scale(garage_4_on, (garage_4_on.get_width() * 0.265, garage_4_on.get_height() * 0.265))
    garage_5_on = pygame.image.load("images/garage_5_on.png").convert_alpha()
    garage_5_on = pygame.transform.scale(garage_5_on, (garage_5_on.get_width() * 0.26, garage_5_on.get_height() * 0.26))


# all draw calls for lobby screen
def draw(window, player, players, host_id, team_list):
    # make sure server and client data are synced
    # host_id and team_list should never be -1 because this would indicate the client is not in a lobby,
    # but this draw -call can only be occuring if the client screen is set to be in a lobby
    if host_id == -1 or team_list == -1:
        print("client is displaying lobby but server is not sending lobby specific information")
        return
    
    # background draw calls
    window.blit(background_img, (0, 0))

    # light up team numbers if team has members
    if len(team_list[0]) != 0:
        window.blit(garage_1_on, (helper.getScreenX(148), helper.getScreenY(358)))
    if len(team_list[1]) != 0:
        window.blit(garage_2_on, (helper.getScreenX(148 + 318), helper.getScreenY(356)))
    if len(team_list[2]) != 0:
        window.blit(garage_3_on, (helper.getScreenX(148 + 318 * 2 + 10), helper.getScreenY(352)))
    if len(team_list[3]) != 0:
        window.blit(garage_4_on, (helper.getScreenX(148 + 318 * 3 + 8), helper.getScreenY(351.5)))
    if len(team_list[4]) != 0:
        window.blit(garage_5_on, (helper.getScreenX(148 + 318 * 4 + 12), helper.getScreenY(355)))
    
    # button draw calls
    exit_button.draw(window)
    for x in range(5):
        join_team_buttons[x].draw(window)

    # text draw calls
    helper.drawText(window, player.lobbyID, helper.getArialFont(helper.getScreenX(150)), (0, 0, 0),
                    helper.getScreenX(1300), helper.getScreenY(100), True)
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
    global exit, change_team, change_team_value
    # update buttons
    exit_button.update()
    for x in range(5):
        join_team_buttons[x].update()

    # do button actions on release
    if exit_button.click_release:
        print("exit lobby")
        exit = True
        exit_button.click_release = False
    for x in range(5):
        if join_team_buttons[x].click_release:
            print("join team")
            change_team = True
            change_team_value = x
            join_team_buttons[x].click_release = False
            break