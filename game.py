import pygame


class Game:
    def __init__(self):
        pygame.init()
        width, height = (389, 489)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Theoretically")
        self.clock = pygame.time.Clock()
        # set up the board as 6 rows of 5 columns over 3 theaters (space, air, and land)
        self.board = [[[None for x in range(5)] for y in range(6)] for z in range(3)]

    def draw_board(self):
        for x in range(5):
            for y in range(6):
                pygame.draw.rect(self.screen, (255, 255, 255), (50 + 50 * x, 50 + 50 * y, 50, 50), 1)

    def update(self):
        # sleep to make the game 60 fps
        self.clock.tick(60)
        # clear the screen
        self.screen.fill(0)
        self.draw_board()

        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

        # update the screen
        pygame.display.flip()
