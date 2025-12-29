import pygame
from defs import * 
from pipe import PipeCollection
from bird import Bird


def update_data_label(data, title, font, gameDisplay, x, y):
    label = font.render('{} {}'.format(title, data), 1, DATA_FONT_COLOR)
    gameDisplay.blit(label, (x, y))
    return y

def update_data_labels(dt, font, gameDisplay, game_time):
    y_pos = 10
    gap = 20
    x_pos = 10
    y_pos = update_data_label(round(1000/dt, 2), 'FPS', font, gameDisplay, x_pos, y_pos + gap)
    y_pos = update_data_label(round(game_time/1000, 2), 'Game time', font, gameDisplay, x_pos, y_pos + gap)
    

def run_game():
    pygame.init()
    gameDisplay = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption('Learn to fly')

    running = True
    bgImg = pygame.image.load(BG_FILENAME)
    pipes = PipeCollection(gameDisplay)
    pipes.create_new_set()
    bird = Bird(gameDisplay)

    

    label_font = pygame.font.SysFont('monospace', DATA_FONT_SIZE)


    clock = pygame.time.Clock()
    dt = 0
    game_time = 0

    while running:
        
        dt = clock.tick(FPS)
        game_time += dt

        gameDisplay.blit(bgImg, (0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                else:
                    running = False
             
        update_data_labels(dt, label_font, gameDisplay, game_time)
        pipes.update(dt)
        bird.update(dt)

        pygame.display.update()




if __name__ == "__main__":
    run_game()