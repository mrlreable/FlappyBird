import pygame
import os

#global variables
clock = pygame.time.Clock()
WIDTH, HEIGHT = 288, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy bird')
FPS = 120
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
BASE_WIDTH = 336
BASE_HEIGHT = 112
birdPos = pygame.Rect(50, HEIGHT/2, BIRD_WIDTH, BIRD_HEIGHT)
base1Pos = pygame.Rect(0, 450, BASE_WIDTH, BASE_HEIGHT)
base2Pos = pygame.Rect(WIDTH, 450, BASE_WIDTH, BASE_HEIGHT)


#loading images
BACKGROUND = pygame.image.load(os.path.join('assets', 'background-day.png'))
BASE = pygame.image.load(os.path.join('assets', 'base.png'))
BIRD_DOWN = pygame.image.load(os.path.join('assets', 'redbird-downflap.png'))
BIRD_MID = pygame.image.load(os.path.join('assets', 'redbird-midflap.png'))
BIRD_UP = pygame.image.load(os.path.join('assets', 'redbird-upflap.png'))
GAME_OVER = pygame.image.load(os.path.join('assets', 'gameover.png'))
START_SCREEN = pygame.image.load(os.path.join('assets', 'message.png'))
PIPE = pygame.image.load(os.path.join('assets', 'pipe-green.png'))


def moveFloor():
    base1Pos = pygame.Rect(0, 450, BASE_WIDTH, BASE_HEIGHT)
    base2Pos = pygame.Rect(WIDTH, 450, BASE_WIDTH, BASE_HEIGHT)
    WIN.blit(BASE, (base1Pos.x, base1Pos.y))
    WIN.blit(BASE, (base2Pos.x, base2Pos.y))

    base1Pos.x -= 1
    base2Pos.x -= 1

    if base2Pos.x == 0:
        base1Pos.x = WIDTH
    if base1Pos.x == 0:
        base2Pos.x = WIDTH


def draw_window(birdPos, base1Pos, base2Pos):
    WIN.fill((255, 255, 255))

    WIN.blit(BACKGROUND, (0, 0))

    WIN.blit(BASE, (base1Pos.x, base1Pos.y))
    WIN.blit(BASE, (base2Pos.x, base2Pos.y))
    if base2Pos.x == 0:
        base1Pos.x = WIDTH
    if base1Pos.x == 0:
        base2Pos.x = WIDTH

    WIN.blit(BIRD_MID, (birdPos.x, birdPos.y))

    
    pygame.display.update()

def main():
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        VELOCITY = 5
        keysPressed = pygame.key.get_pressed() #gives back a list of bools for the corresponding keys
        if keysPressed[pygame.K_SPACE]:
            birdPos.y -= VELOCITY
            

        base1Pos.x -= 1
        base2Pos.x -= 1

        draw_window(birdPos, base1Pos, base2Pos)

    pygame.quit()

if __name__ == '__main__':
    main()
