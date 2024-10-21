#Johnathan Stormes 2024
import pygame
import random
import helper

class Player:
    def __init__(self, ID):
        self.ID = ID
        self.lobbyID = ""
        self.team = -1
        # movement (TEMP)
        self.x = helper.CLIENT_SCREEN_WIDTH / 2
        self.y = helper.CLIENT_SCREEN_HEIGHT / 2
        self.width = 50
        self.height = 50
        self.velocity = 6
        self.rect = (self.x, self.y, self.width, self.height)
        self.border_rect = (self.x, self.y, self.width, self.height)
        self.r = random.randrange(1, 255)
        self.g = random.randrange(1, 255)
        self.b = random.randrange(1, 255)
    
    # mutators
    def setLobby(self, lobbyID):
        self.lobbyID = lobbyID
    def setTeam(self, team):
        self.team = team

    # accessors
    def getLobby(self):
        return self.lobbyID
    def getTeam(self):
        return self.team
    def getID(self):
        return self.ID
    
    # movement (TEMP)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.velocity
        if keys[pygame.K_d] and self.x < helper.CLIENT_SCREEN_WIDTH - self.width:
            self.x += self.velocity
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.velocity
        if keys[pygame.K_s] and self.y< helper.CLIENT_SCREEN_HEIGHT - self.height:
            self.y += self.velocity
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        self.border_rect = (self.x, self.y, self.width, self.height)
    def draw(self, window, host_id, is_client, team_list):
        # draw moving square for player
        if is_client:
            self.rect = (self.x + 5, self.y + 5, self.width - 10, self.height - 10)
            pygame.draw.rect(window, (255, 255, 0), self.border_rect)
        pygame.draw.rect(window, (self.r, self.g, self.b), self.rect)
        
        # draw player square on team garage
        team = -1
        index = -1
        for x in range(len(team_list)):
            for y in range(len(team_list[x])):
                if team_list[x][y].ID == self.ID:
                    team = x
                    index = y
        if index == 0 and team != -1:
            garage_rect = (helper.CLIENT_SCREEN_WIDTH / 10 * (1 + team * 2) - 75, helper.getScreenY(450), 50, 50)
        if index == 1 and team != -1:
            garage_rect = (helper.CLIENT_SCREEN_WIDTH / 10 * (1 + team * 2) + 25, helper.getScreenY(450), 50, 50)
        pygame.draw.rect(window, (self.r, self.g, self.b), garage_rect)

        # draw host and ID text
        if self.ID == host_id:
            helper.drawText(window, "host", helper.getArialFont(helper.getScreenX(20)), (0, 0, 0), self.x, self.y - 30)
        helper.drawText(window, str(self.ID), helper.getArialFont(helper.getScreenX(20)), (0, 0, 0), self.x, self.y + self.height)
        helper.drawText(window, str(self.ID), helper.getArialFont(helper.getScreenX(20)), (0, 0, 0)
                        , garage_rect[0], helper.getScreenY(460))