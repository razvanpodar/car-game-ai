import pygame

class Game:

    WINDOW_NAME = "Dodgecar"
    WIDTH = 480
    HEGHT = 640
    FRAME_RATE = 60
    LANE_COUNT = 3

    def __init__(self):
        self.lanes = [0] * self.LANE_COUNT
        self.lane_width = self.WIDTH / self.LANE_COUNT
        self.running = True
        
        for i, lane in enumerate(self.lanes):
            self.lanes[i] = self.lane_width * i

        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEGHT))
        pygame.display.set_caption(self.WINDOW_NAME)

    def run(self):
        while (self.running):
            self.window.fill(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

if __name__ == "__main__":
    game = Game()
    game.run()