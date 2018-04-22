import pygame

class Tile:
    def __init__(self, h, w, bg, chara, posX, posY, move):
        self.height = h
        self.width = w

        # background image (string of image in directory)
        self.background = bg

        # character object
        self.character = chara

        self.posX = posX
        self.posY = posY
        self.move = move
        self.isfilled = False


        self.highlighted = False

    def changeHightlighted(self, BOOL):
        self.highlighted = BOOL
    def isHighlighted(self):
        return self.highlighted



    def changeBackground(self, background):
        self.background = pygame.image.load(background)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def changeCharacter(self, character):
        self.character = character
        if character is 0:
            return
        else:
            self.character.image = pygame.transform.scale(self.character.image, (self.width, self.height))

    def changeMove(self, move):
        self.move = move

    def isFilled(self):
        return self.isfilled