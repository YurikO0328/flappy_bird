import pygame
import random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bird Up only")

bird_img = pygame.image.load("img\\bird1.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_img
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= 5

bird_group = pygame.sprite.Group()
bird = Bird(100, int(screen_height/ 2))
bird_group.add(bird)

run = True
while run:
    clock.tick(fps)

    screen.fill((0,0,0))

    bird_group.draw(screen)
    bird_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()