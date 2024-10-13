# Johnathan Stormes
import pygame
import helper

class Button():
    def __init__(self, x, y, image, image_pressed, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (int(helper.getScreenX(self.width)), int(helper.getScreenY(self.height))))
        self.image_pressed = pygame.transform.scale(image_pressed, (int(helper.getScreenX(self.width)), int(helper.getScreenY(self.height))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (helper.getScreenX(self.x), helper.getScreenY(self.y))
        self.clicked = False
        self.click_release = False

    # updates the clicked variable
    def update(self):
        # get position of mouse
        pos = pygame.mouse.get_pos()

        # check if mouse clicked on button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            if (self.clicked == True):
                self.click_release = True
            self.clicked = False

        # resize image and rect when screen is resized
        self.image = pygame.transform.scale(self.image, (int(helper.getScreenX(self.width)), int(helper.getScreenY(self.height))))
        self.image_pressed = pygame.transform.scale(self.image_pressed, (int(helper.getScreenX(self.width)), int(helper.getScreenY(self.height))))
        self.rect = self.image.get_rect()
        self.rect.topleft = (helper.getScreenX(self.x), helper.getScreenY(self.y))

    # draws the button when called
    def draw(self, window):
        # draw the button
        if self.clicked:
            window.blit(self.image_pressed, (self.rect.x, self.rect.y))
            return
        window.blit(self.image, (self.rect.x, self.rect.y))