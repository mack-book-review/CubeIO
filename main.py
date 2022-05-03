import pygame, sys, random, time
from pygame.locals import *
from cube import Cube

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Cube.io Game")

cubeSize = 20

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

food = [random.randint(1, 480), random.randint(1, 480), 20, 20]
Bfood = [random.randint(1, 480), random.randint(1, 480), 20, 20]


cube = Cube(250,250,20,5)
run = True

while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        cube.move_right()

    if keys[pygame.K_LEFT]:
        cube.move_left()

    if keys[pygame.K_UP]:
        cube.move_up()

    if keys[pygame.K_DOWN]:
         cube.move_down()

    screen.fill(WHITE)

    cube.draw(screen)

    food_status = True
    Bfood_status = True

    if cube.rect.colliderect(food):
        cube.rect.width += 10
        cube.rect.height += 10
        food_status = False

    if cube.rect.colliderect(Bfood):
        cube.rect.width -= 10
        cube.rect.height -= 10
        Bfood_status = False

    if not food_status:
        food = [random.randint(1, 480), random.randint(1, 480), 20, 20]

    if not Bfood_status:
        Bfood = [random.randint(1, 480), random.randint(1, 480), 20, 20]

    pygame.draw.rect(screen, YELLOW, pygame.Rect(food))
    pygame.draw.rect(screen, GREEN, pygame.Rect(Bfood))

    pygame.display.update()
pygame.quit()




