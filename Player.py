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
        self.y = helper.getScreenY(700)
        self.velocity = 6
        self.radius = helper.getScreenX(35)
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
        if keys[pygame.K_a] and self.x > self.radius:
            self.x -= self.velocity
        if keys[pygame.K_d] and self.x < helper.CLIENT_SCREEN_WIDTH - self.radius:
            self.x += self.velocity
        if keys[pygame.K_w] and self.y > self.radius + helper.getScreenY(540):
            self.y -= self.velocity
        if keys[pygame.K_s] and self.y< helper.CLIENT_SCREEN_HEIGHT - self.radius:
            self.y += self.velocity
        self.update()

    def update(self):
        pass

    def draw(self, window, host_id, is_client, team_list):
        # draw moving square for player
        if is_client:
            pygame.draw.circle(window, (255, 255, 0), (self.x, self.y), self.radius)
            pygame.draw.circle(window, (self.r, self.g, self.b), (self.x, self.y), self.radius - 5)
        else:
            pygame.draw.circle(window, (self.r, self.g, self.b), (self.x, self.y), self.radius)
        
        # draw player square on team garage
        team = -1
        index = -1
        for x in range(len(team_list)):
            for y in range(len(team_list[x])):
                if team_list[x][y].ID == self.ID:
                    team = x
                    index = y
        garage_y = helper.getScreenY(480)
        if index == 0 and team != -1:
            garage_x = helper.CLIENT_SCREEN_WIDTH / 10 * (1 + team * 2) - self.radius - 15
        if index == 1 and team != -1:
            garage_x = helper.CLIENT_SCREEN_WIDTH / 10 * (1 + team * 2) + self.radius + 15
        pygame.draw.circle(window, (self.r, self.g, self.b), (garage_x, garage_y), self.radius)

        # draw host and ID text
        if self.ID == host_id:
            helper.drawText(window, "host", helper.getArialFont(helper.getScreenX(20)), (0, 0, 0), self.x, self.y - self.radius - 15, True)
        helper.drawText(window, str(self.ID), helper.getArialFont(helper.getScreenX(20)), (0, 0, 0), self.x, self.y, True)
        helper.drawText(window, str(self.ID), helper.getArialFont(helper.getScreenX(20)), (0, 0, 0)
                        , garage_x, helper.getScreenY(480), True)