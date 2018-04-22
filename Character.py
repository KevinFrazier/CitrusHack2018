import pygame

class Character:
    def __init__(self, image, hp, atk, mp, abilities, movement, rge, id):
        self.hp = hp
        self.atk = atk
        self.mp = mp
        self.abilities = abilities
        self.movement = movement
        self.range = rge
        self.image = pygame.image.load(image)
        self.id = id
        self.hasMoved = False