import pygame

class Player:
    
    SPRITE_PATH = "../res/sprites/player.png"

    def __init__(self, x, y, lane):
        self.pos = (x, y)
        self.lane = lane
        self.sprite = pygame.image.load(self.SPRITE_PATH)

    def move(self, x, y, lane):
        self.pos = (x, y)
        self.lane = lane