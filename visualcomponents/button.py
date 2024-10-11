# Johnathan Stormes
import pygame
import helper

class Button():
    def __init__(self, x, y, image, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (int(helper.getScreenX(self.width)), int(helper.getScreenY(self.height))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (helper.getScreenX(self.x), helper.getScreenY(self.y))
        self.clicked = False

    # updates the clicked variable
    def update(self):
        # get position of mouse
        pos = pygame.mouse.get_pos()

        # check if mouse clicked on button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print("hit")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # resize image and rect when screen is resized
        self.image = pygame.transform.scale(self.image, (int(helper.getScreenX(self.width)), int(helper.getScreenY(self.height))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (helper.getScreenX(self.x), helper.getScreenY(self.y))

    # draws the button when called
    def draw(self, window):
        # draw the button
        window.blit(self.image, (self.rect.x, self.rect.y))