#Johnathan Stormes 2024
import pygame
import random

class Player:
    def __init__(self, ID):
        self.ID = ID
        self.lobbyID = ""
        self.team = -1
        # movement (TEMP)
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.velocity = 3
        self.rect = (self.x, self.y, self.width, self.height)
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
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_UP]:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.y += self.velocity
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
    def draw(self, window):
        pygame.draw.rect(window, (self.r, self.g, self.b), self.rect)