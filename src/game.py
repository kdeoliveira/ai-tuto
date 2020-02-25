import neat
import time

from bird import *
from pipe import *

WIN_HEIGTH = 600
WIN_WIDTH = 800

pygame.init()

def draw_window(win, bird):
    win.blit(BG_IMG, (0,0))
    bird.draw(win)
    pygame.display.update()


def main():
    bird = Bird(200, 200)
    win = pygame.display.set_mode((WIN_HEIGTH, WIN_WIDTH))

    #Clock for FPS
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        bird.move()
        draw_window(win, bird)

    pygame.quit()
    quit()
main()




