import pygame

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Cube:


    def __init__(self,x,y,size,speed):
        self.rect = pygame.Rect(x,y,size,size)
        self.speed = speed
        self.color_change_size = 100

    def move_right(self):
        if self.rect.left >= 500 - self.rect.width:
            self.rect.left = 500 - self.rect.width
        else:
            self.rect.left += self.speed

    def move_left(self):
        if self.rect.left < 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def move_up(self):
        if self.rect.top < 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def move_down(self):
        if self.rect.bottom > 500:
            self.rect.bottom = 500
        else:
            self.rect.bottom += self.speed

    def draw(self,screen):
        if self.rect.width <= self.color_change_size:
            pygame.draw.rect(screen, RED, self.rect)
        else:
            pygame.draw.rect(screen, BLUE, self.rect)

