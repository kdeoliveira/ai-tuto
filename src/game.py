import neat
import time

from pipe import *
pygame.init()
pygame.font.init()

WIN_HEIGTH = 600
WIN_WIDTH = 800
STAT_FONT = pygame.font.SysFont("comicsans", 50)

def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0,0))
    for pipe in pipes:
        pipe.draw(win)
    base.draw(win)
    bird.draw(win)
    
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    pygame.display.update()


def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(INIT_X)]
    win = pygame.display.set_mode((WIN_HEIGTH, WIN_WIDTH))
    score = 0

    #Clock for FPS
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        # global score
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        add_pipe = False
        rm = []
        for pipe in pipes:
            if pipe.collide(bird):
                print("collision")
                pass

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rm.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()
        
        if add_pipe:
            score += 1
            pipes.append(Pipe(INIT_X))
        
        for r in rm:
            pipes.remove(r)

        # 
        if bird.y + bird.img.get_height() >= 730:
            if not(add_pipe):
                print("Ground hit")
            pass

        # bird.move()
        base.move()
        draw_window(win, bird, pipes, base, score)

    pygame.quit()
    quit()
main()




