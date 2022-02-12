import pygame
from player import Player

class Game:

    WINDOW_NAME = "Dodgecar"
    WIDTH = 480
    HEIGHT = 640
    FRAME_RATE = 60
    LANE_COUNT = 3

    def __init__(self):
        self.lanes = [0] * self.LANE_COUNT
        self.lane_width = self.WIDTH / self.LANE_COUNT
        self.running = True
        self.score = 0
        
        for i, lane in enumerate(self.lanes):
            self.lanes[i] = self.lane_width * i

        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.WINDOW_NAME)

        self.player = Player(self.lanes[1], self.HEIGHT - 100, 1)

    def run(self):
        while (self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.window.fill(0)
            self.window.blit(self.player.sprite, self.player.pos)
            pygame.display.flip()
            

if __name__ == "__main__":
    game = Game()
    game.run()